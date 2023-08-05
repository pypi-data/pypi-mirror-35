# -*- coding: utf-8 -*-

"""Check the given directories for regressions

Currently intended only for use with FITS files
"""

from glob import iglob as glob
import itertools
import os
from pprint import pprint

from astropy.io import fits
from deepdiff import DeepDiff


def get_all_files_of_type(path, patterns):
    """Given a path and a collection of globs, return relative paths of all matching files"""

    # Handle multiple globs
    results = itertools.chain.from_iterable(
        glob(os.path.join(path, pattern)) for pattern in patterns
    )

    # Remove the "base" portion from each path, convert to set, return
    return set([result[len(path) + 1 :] for result in results])


def diff_dirs(original_path, new_paths, patterns):
    _diffs = []

    # Build a list of all FITS files in the "original" path
    original_path_fits_files = get_all_files_of_type(original_path, patterns)

    # Build a dict of {path: list of all FITS files in path} for each "new" path
    new_paths_to_fits_files = dict()
    for new_path in new_paths:
        new_path_fits_files = get_all_files_of_type(new_path, patterns)
        new_paths_to_fits_files[new_path] = new_path_fits_files
        # Check for differences between the "new" path and the "original" path. Note
        # that we are diffing sets here
        diff = DeepDiff(original_path_fits_files, new_path_fits_files)
        if diff:
            print(
                "Differences detected between directory trees {} and {}".format(
                    original_path, new_path
                )
            )
            pprint(diff)
            _diffs.append((original_path, new_path))

    for relative_fits_file_path in original_path_fits_files:
        full_old_fits_file_path = os.path.join(original_path, relative_fits_file_path)
        print("Comparing {} with:".format(full_old_fits_file_path))
        old_fits_hdu = fits.open(full_old_fits_file_path)
        for new_path in new_paths_to_fits_files:
            full_new_fits_file_path = os.path.join(new_path, relative_fits_file_path)
            try:
                new_fits_hdu = fits.open(full_new_fits_file_path)
            except FileNotFoundError:
                print(
                    "  {} does not exist, but should!".format(full_new_fits_file_path)
                )
                _diffs.append((relative_fits_file_path, full_new_fits_file_path))
            else:
                print("  {}".format(full_new_fits_file_path))
                diff = fits.FITSDiff(
                    old_fits_hdu,
                    new_fits_hdu,
                    ignore_keywords=["DATE", "DATE-MAP"],
                )
                if diff:
                    print("Are different:")
                    print(diff.report())
                    print("-" * 30)
                    _diffs.append((relative_fits_file_path, full_new_fits_file_path))

    return _diffs
