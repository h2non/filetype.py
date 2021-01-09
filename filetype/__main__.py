import filetype


def guess(path):
    kind = filetype.guess(path)
    if kind is None:
        print('{}: File type determination failure.'.format(path))
    else:
        print('{}: {} ({})'.format(path, kind.extension, kind.mime))


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Determine type of FILEs.')
    parser.add_argument("file", nargs='+')
    parser.add_argument('-v', '--version', action='store_true',
                        help='output version information and exit')
    args = parser.parse_args()

    if args.version:
        print(filetype.version)
    else:
        for i in args.file:
            guess(i)


if __name__ == '__main__':
    main()
