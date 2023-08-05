#!/usr/bin/env python
# Evan Widloski - 2018-08-07
# Script for reading time offsets from Trodes .time.dat files

from __future__ import print_function
import struct
import os
import argparse
import re

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Extract time offsets (in samples) from Trodes .time.dat files for the mountainsort ms3_drifttag.mlp pipeline")
    parser.add_argument('dat_file', type=str, help="path to Trodes .time.dat file")
    parser.add_argument('--total_duration', action='store_true', help="return total duration (in samples) instead")

    args = parser.parse_args()

    with open(args.dat_file, 'rb') as f:
        segments_search = re.search(b'Fields: <timeperiods ([0-9]+)\*uint32>', f.read())

        assert segments_search, "Problem reading number of segments from .dat file"

        segments = int(segments_search.group(1))
        f.seek(-8 * segments, os.SEEK_END)
        b = f.read(8 * segments)
        timepoints = struct.unpack('<' + 'L' * segments * 2, b)

    startpoints = timepoints[0::2]
    endpoints = timepoints[1::2]


    offsets = [0]
    for start, end in zip(startpoints, endpoints):
        offsets.append(end - start)

    if args.total_duration:
        print(sum(offsets), end='')
    else:
        print(','.join([str(offset) for offset in offsets]))
