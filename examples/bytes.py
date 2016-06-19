import filetype


def main():
    buf = bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08])
    kind = filetype.guess_type(buf)

    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)


if __name__ == '__main__':
    main()
