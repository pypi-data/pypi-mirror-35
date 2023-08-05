#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Command Line Interface for diffdirs"""

import argparse
from pprint import pprint

from .diffdirs import diff_dirs


def parse_args():
    """Parse arguments"""

    parser = argparse.ArgumentParser(prog="diffdirs")
    parser.add_argument(
        "original_data_path",
        metavar="ORIGINAL_DATA_PATH",
        help="The path to the 'original' data. This will be used to compare against",
    )
    parser.add_argument(
        "new_data_paths",
        metavar="NEW_DATA_PATH",
        nargs="+",
        help="The path(s) to the 'new' data. These will be compared against original_data_path",
    )
    parser.add_argument(
        "-g",
        "--globs",
        metavar="GLOB",
        default=["**/*.fits"],
        nargs="+",
        help=(
            "An optional glob pattern for specifying which files to check for regression"
            "NOTE: This currently will only work for FITS files"
        ),
    )

    return parser.parse_args()


def main():
    """Entry point"""

    args = parse_args()
    print(args.globs)
    diffs = diff_dirs(args.original_data_path, args.new_data_paths, args.globs)
    print("DIFFS:")
    pprint(diffs)


if __name__ == "__main__":
    main()
