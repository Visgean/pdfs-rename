#!/usr/bin/env python3

from pathlib import Path

import argparse
import shutil

from . import utils

parser = argparse.ArgumentParser(description="Renames all whacky PDF named files to a bit better form.")
parser.add_argument('pdfs', nargs='+', help='list of filenames to rename')
parser.add_argument('--rename', dest='rename', action='store_true', help='rename the files, on default we only print extracted filenames')
parser.add_argument('--extract', dest='extract', action='store_true', help='extract new name from text')


def main():
    args = parser.parse_args()
    for filename in args.pdfs:
        abs_path = Path(filename).resolve()
        base_dir = abs_path.parent

        if args.extract:
            new = utils.extract_from_title(filename)
        else:
            new  = utils.extract_from_metadata(filename)

        if new is None:
            print(f"Skipping {filename}, could not find better name")
            continue

        print(f"Original {filename}, new name: {new}")

        if not args.rename:
            continue

        new_abs_path = base_dir / Path(new)

        if new_abs_path.exists():
            print(f'{new_abs_path} already exists, skipping')
            continue
        shutil.move(filename, new_abs_path)


if __name__ == '__main__':
    main()