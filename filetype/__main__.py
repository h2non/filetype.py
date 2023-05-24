import glob
from itertools import chain
from os.path import isfile

import filetype


def guess(path):
    kind = filetype.guess(path)
    if kind is None:
        print('{}: File type determination failure.'.format(path))
    else:
        print('{}: {} ({})'.format(path, kind.extension, kind.mime))


def main():
    import argparse

    parser = argparse.ArgumentParser(
        prog='filetype', description='Determine type of FILEs.'
    )
    parser.add_argument(
        'file', nargs='+',
        help='files, wildcard is supported'
    )
    parser.add_argument(
        '-v', '--version', action='version',
        version=f'%(prog)s {filetype.version}',
        help='output version information and exit'
    )

    args = parser.parse_args()
    items = chain.from_iterable(map(glob.iglob, args.file))
    files = filter(isfile, items)

    for file in files:
        guess(file)


if __name__ == '__main__':
    main()
