# A simple async IPFS client demonstrating basic usage of the API

import sys, os, os.path
import argparse
import tempfile
import pprint

from tqdm import trange, tqdm

import asyncio
import aiofiles
import aiohttp
import aioipfs

async def tasks_with_progress(tasks):
    responses = []
    for f in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
        responses.append(await f)
    return responses

async def get_verbose(cli, hash, tmpd):
    lock = asyncio.Lock()
    async def progcb(mhash, readsofar, arg):
        lock = arg
        await asyncio.sleep(0.00)
        if divmod(readsofar, 4096*32)[1] == 0:
            prog = '{0} {1}'.format(mhash, readsofar)

    return await cli.get(hash, dstdir=tmpd, progress_callback=progcb,
            progress_callback_arg=lock)

async def pin_add(cli, hash, tmpd):
    async for pinned in cli.pin.add(hash):
        if 'Pins' in pinned:
            print('Pinned', pinned['Pins'][0])

async def get_multi(cli, hashes, tmpd):
    tasks = [ get_verbose(cli, hash, tmpd) for hash in hashes ]
    return await tasks_with_progress(tasks)

async def pin_add_multi(cli, hashes, tmpd):
    tasks = [ pin_add(cli, hash, tmpd) for hash in hashes ]
    return await tasks_with_progress(tasks)

async def log_tail(cli):
    async for msg in cli.log.tail():
        print(pprint.pprint(msg))

async def asyncipfs_main(args):
    async with aioipfs.AsyncIPFS(host=args.apihost,
            port=args.apiport) as cli:
        if args.subparser_name == 'get':
            tmpd = tempfile.mkdtemp()
            print('Destination directory:', tmpd)
            gathered = await get_multi(cli, args.multihash, tmpd)
            await cli.close()
            return gathered

        if args.subparser_name == 'pin_add':
            tmpd = tempfile.mkdtemp()
            gathered = await pin_add_multi(cli, args.multihash, tmpd)
            await cli.close()
            return gathered

        if args.subparser_name == 'log':
            await log_tail(cli)
            await cli.close()

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", default=False,
            help = "Enable debugging")
    parser.add_argument("--apihost", default='localhost', metavar='str',
            help = "IPFS API host")
    parser.add_argument("--apiport", default=5001, metavar='str',
            help = "IPFS API port")

    subparsers = parser.add_subparsers(dest='subparser_name',
            help='sub-command help')
    parser_get = subparsers.add_parser('get', help='Get files from IPFS')
    parser_get.add_argument("multihash", nargs='+', help="Multihash")

    parser_log = subparsers.add_parser('log', help='View daemon logs')

    parser_pin_add = subparsers.add_parser('pin_add', help='Pin a resource')
    parser_pin_add.add_argument("multihash", nargs='+', help="Multihash")

    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncipfs_main(args))
