import filetype


def main():
    f = open('tests/fixtures/sample.jpg', 'rb')
    data = f.read()

    kind = filetype.guess_type(data)
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)


if __name__ == '__main__':
    main()
