#!/usr/bin/env python3

import sqlite3
import sys
import zstd
import click
from functools import partial
from pathlib import Path
from blspy import AugSchemeMPL, G1Element

from typing import Callable, Optional, Union, List
from time import time

from chia_rs import run_generator, MEMPOOL_MODE

from chia.types.blockchain_format.program import Program
from chia.consensus.default_constants import DEFAULT_CONSTANTS
from chia.wallet.puzzles.rom_bootstrap_generator import get_generator
from chia.util.full_block_utils import block_info_from_block, generator_from_block
from chia.util.condition_tools import pkm_pairs
from chia.types.full_block import FullBlock
from chia.types.blockchain_format.sized_bytes import bytes32, bytes48
from chia.types.block_protocol import BlockInfo

GENERATOR_ROM = bytes(get_generator())


# returns an optional error code and an optional PySpendBundleConditions (from chia_rs)
# exactly one of those will hold a value and the number of seconds it took to
# run
def run_gen(env_data: bytes, block_program_args: bytes, flags: int):
    max_cost = DEFAULT_CONSTANTS.MAX_BLOCK_COST_CLVM
    cost_per_byte = DEFAULT_CONSTANTS.COST_PER_BYTE

    # we don't charge for the size of the generator ROM. However, we do charge
    # cost for the operations it executes
    max_cost -= len(env_data) * cost_per_byte

    env_data = b"\xff" + env_data + b"\xff" + block_program_args + b"\x80"

    try:
        start_time = time()
        err, result = run_generator(
            GENERATOR_ROM,
            env_data,
            max_cost,
            flags,
        )
        run_time = time() - start_time
        return err, result, run_time
    except Exception as e:
        # GENERATOR_RUNTIME_ERROR
        sys.stderr.write(f"Exception: {e}\n")
        return 117, None, 0


def callable_for_module_function_path(call: str) -> Callable:
    module_name, function_name = call.split(":", 1)
    module = __import__(module_name, fromlist=[function_name])
    return getattr(module, function_name)


@click.command()
@click.argument("file", type=click.Path(), required=True)
@click.option(
    "--mempool-mode", default=False, is_flag=True, help="execute all block generators in the strict mempool mode"
)
@click.option("--verify-signatures", default=False, is_flag=True, help="Verify block signatures (slow)")
@click.option("--start", default=225000, help="first block to examine")
@click.option("--end", default=None, help="last block to examine")
@click.option("--call", default=None, help="function to pass block iterator to in form `module:function`")
def main(file: Path, mempool_mode: bool, start: int, end: Optional[int], call: Optional[str], verify_signatures: bool):

    call_f: Callable[[Union[BlockInfo, FullBlock], bytes32, int, List[bytes], float, int], None]
    if call is None:
        call_f = partial(default_call, verify_signatures)
    else:
        call_f = callable_for_module_function_path(call)

    c = sqlite3.connect(file)

    end_limit_sql = "" if end is None else f"and height <= {end} "

    rows = c.execute(
        f"SELECT header_hash, height, block FROM full_blocks "
        f"WHERE height >= {start} {end_limit_sql} and in_main_chain=1 ORDER BY height"
    )

    for r in rows:
        hh: bytes32 = r[0]
        height: int = r[1]
        block: Union[BlockInfo, FullBlock]
        if verify_signatures:
            block = FullBlock.from_bytes(zstd.decompress(r[2]))
        else:
            block = block_info_from_block(zstd.decompress(r[2]))

        if block.transactions_generator is None:
            sys.stderr.write(f" no-generator. block {height}\r")
            continue

        start_time = time()
        generator_blobs = []
        for h in block.transactions_generator_ref_list:
            ref = c.execute("SELECT block FROM full_blocks WHERE height=? and in_main_chain=1", (h,))
            generator = generator_from_block(zstd.decompress(ref.fetchone()[0]))
            assert generator is not None
            generator_blobs.append(bytes(generator))
            ref.close()

        ref_lookup_time = time() - start_time

        flags: int
        if mempool_mode:
            flags = MEMPOOL_MODE
        else:
            flags = 0

        call_f(block, hh, height, generator_blobs, ref_lookup_time, flags)


def default_call(
    verify_signatures: bool,
    block: Union[BlockInfo, FullBlock],
    hh: bytes32,
    height: int,
    generator_blobs: List[bytes],
    ref_lookup_time: float,
    flags: int,
) -> None:
    num_refs = len(generator_blobs)

    # add the block program arguments
    block_program_args = bytearray(b"\xff")
    for ref_block_blob in generator_blobs:
        block_program_args += b"\xff"
        block_program_args += Program.to(ref_block_blob).as_bin()
    block_program_args += b"\x80\x80"

    assert block.transactions_generator is not None
    err, result, run_time = run_gen(bytes(block.transactions_generator), bytes(block_program_args), flags)
    if err is not None:
        sys.stderr.write(f"ERROR: {hh.hex()} {height} {err}\n")
        return

    num_removals = len(result.spends)
    fees = result.reserve_fee
    cost = result.cost
    num_additions = 0
    for spends in result.spends:
        num_additions += len(spends.create_coin)

    if verify_signatures:
        assert isinstance(block, FullBlock)
        # create hash_key list for aggsig check
        pairs_pks: List[bytes48] = []
        pairs_msgs: List[bytes] = []
        pairs_pks, pairs_msgs = pkm_pairs(result, DEFAULT_CONSTANTS.AGG_SIG_ME_ADDITIONAL_DATA)
        pairs_g1s = [G1Element.from_bytes(x) for x in pairs_pks]
        assert block.transactions_info is not None
        assert block.transactions_info.aggregated_signature is not None
        assert AugSchemeMPL.aggregate_verify(pairs_g1s, pairs_msgs, block.transactions_info.aggregated_signature)

    print(
        f"{hh.hex()}\t{height:7d}\t{cost:11d}\t{run_time:0.3f}\t{num_refs}\t{ref_lookup_time:0.3f}\t{fees:14}\t"
        f"{len(bytes(block.transactions_generator)):6d}\t"
        f"{num_removals:4d}\t{num_additions:4d}"
    )


if __name__ == "__main__":
    # pylint: disable = no-value-for-parameter
    main()
