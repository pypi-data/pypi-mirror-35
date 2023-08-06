# Simple tool to search for files/directories on your IPFS node

import sys
import os
import re
import argparse
import json

import asyncio
import aioipfs

class HashTracker(object):
    def __init__(self):
        self.hashes = []
        self.lock = asyncio.Lock()

    async def reset(self):
        async with self.lock:
            self.hashes = []

    async def add(self, h):
        async with self.lock:
            self.hashes.append(h)

    async def exists(self, h):
        async with self.lock:
            return h in self.hashes

class Results(object):
    def __init__(self):
        self.__objs = {}

    def __add__(self, obj):
        if not 'Hash' in obj or not obj:
            raise Exception('hash missing')
        ohash = obj['Hash']
        if ohash in self.__objs:
            return self
        self.__objs[ohash] = obj
        return self

    def all(self):
        return self.__objs

def is_file(obj):
    return obj['Type'] == 2

def is_dir(obj):
    return obj['Type'] == 1

async def matches(client, obj, **kwargs):
    # Checks whether an object matches the search parameters

    find_name  = kwargs.get('find_name', None)
    find_type  = kwargs.get('find_type', None)
    find_contains  = kwargs.get('find_contains', None)
    find_insensitive = kwargs.get('find_insensitive', False)

    reflags = 0
    conds = {}

    if find_insensitive:
        reflags = re.IGNORECASE

    if obj['Name']:
        if find_name:
            conds['find_name'] = 1
            ma = re.search(find_name, obj['Name'], reflags)
            if ma:
                conds.pop('find_name')
        if find_type:
            conds['find_type'] = 1
            if is_dir(obj) and find_type == 'd':
                conds.pop('find_type')
            if is_file(obj) and find_type == 'f':
                conds.pop('find_type')

    if is_file(obj) and find_contains:
        conds['find_contains'] = 1
        try:
            data = await client.cat(obj['Hash'])
        except aioipfs.APIException as exc:
            return False
        try:
            data_decoded = data.decode()
        except:
            return False
        ma = re.search(find_contains, data_decoded, reflags)
        if ma:
            conds.pop('find_contains')

    return len(conds.keys()) == 0

async def ipfs_walk(client, htracker, results, roothash, parent, **kwargs):
    if await htracker.exists(roothash):
        return
    await htracker.add(roothash)

    try:
        dir_contents = await client.ls(roothash)
    except aioipfs.APIException as exc:
        return

    if not 'Objects' in dir_contents:
        return

    for objs in dir_contents['Objects']:
        for obj in objs['Links']:
            m = await matches(client, obj, **kwargs)
            if m:
                results += obj

            obj_hash = obj['Hash']
            obj_name = obj['Name']
            await htracker.add(obj_hash)

            if obj['Type'] == 1: # Directory
                await ipfs_walk(client, htracker, results,
                        obj_hash, obj['Name'], **kwargs)
            elif obj["Type"] == 2: # File
                continue

async def find(client, args):
    htracker = HashTracker()
    results = Results()

    async for jref in client.refs.local():
        if 'Ref' not in jref:
            continue

        ref = jref['Ref']
        r = await ipfs_walk(client, htracker, results, ref, None,
                find_name=args.name,
                find_type=args.type,
                find_contains=args.contains,
                find_insensitive=args.insensitive)

    results_list = list(results.all().values())

    if args.jsonoutput:
        print(json.dumps(results_list, indent=4))
    else:
        # No JSON, just the hashes
        for obj in results_list:
            print(obj['Hash'])

async def ipfs_find_main(args):
    client = aioipfs.AsyncIPFS(host=args.apihost,
            port=args.apiport)

    await find(client, args)
    await client.close()

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apihost", default='localhost', metavar='str',
            help = "IPFS API host")
    parser.add_argument("--apiport", default=5001, metavar='str',
            help = "IPFS API port")

    parser.add_argument("-j", action='store_true',
            dest='jsonoutput', help='JSON output')
    parser.add_argument("-i", action='store_true',
            dest='insensitive', help='Case-insensitive match')
    parser.add_argument("--name", help="Match object name")
    parser.add_argument("--type",
        help="Match object type ('d' for directory, 'f' for file)")
    parser.add_argument("--contains", help="Match object content")

    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(ipfs_find_main(args))
