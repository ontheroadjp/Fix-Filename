#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
from pathlib import Path
import glob
import unicodedata

SELF = os.path.basename(__file__)

def _init():
    parser = argparse.ArgumentParser(
        prog = SELF
        , usage='python ' + SELF +  '<dir>'
        , description = 'This script fix filename.'
        , epilog='end'
        , add_help=True
    )
    parser.add_argument('directory'
        , type = Path
        , default = '.'
        , help = 'Target directory'
    )
    parser.add_argument('extension'
        , type = str
        , default = 'md'
        , help = 'Target file extension'
    )
    parser.add_argument('-r', '--recursive'
        , default = False
        , action = 'store_true'
        , help = 'Show operating info'
    )
    parser.add_argument('-v', '--verbose'
        , default = False
        , action = 'store_true'
        , help = 'Show operating steps'
    )
    args = parser.parse_args()
    return args

def _get_files(dir, ext='md'):
    """search all dirs and files"""
    result = { 'dirs': [], 'files': [] }
    for root, dirs, files in os.walk(top=dir):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            result['dirs'].append(dir_path)
#            print(f'{dir_path=}')

        for file in files:
            if not file.lower().endswith(f".{ext}"):
                continue
            file_path = os.path.join(root, file)
            result['files'].append(file_path)
#            print(f'{file_path=}')
    return result

def _normarize(filepath, verbose=False):
    """fix word"""
    dir_path = os.path.dirname(filepath)
    old = os.path.basename(filepath)
    new = unicodedata.normalize("NFKC", old).replace(' ', '_')
    old_path = os.path.join(dir_path, old)
    new_path = os.path.join(dir_path, new)
    os.rename(old_path, new_path)
    if verbose:
        print(bool(old != new), end = ': ')
        print(old, end = ' => ')
        print(new)


def main(ini):
    if ini.recursive:
        result = _get_files(ini.directory, ini.extension)
        files = result['files']
    else:
        files = glob.glob(
            os.path.join(ini.directory, f"*.{ini.extension}")
        )

    for file in files:
        _normarize(file, ini.verbose)

    if not len(files):
        print('no match files.')
    else:
        print(f"{len(files)} files matched.")

main(_init())
print('All done.')
