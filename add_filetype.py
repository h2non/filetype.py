from __future__ import absolute_import

import argparse
import os
import sys
from contextlib import contextmanager

from jinja2 import Template


@contextmanager
def replace(path):
    with open(path) as f:
        content = f.readlines()

    yield content

    with open(path, 'w') as f:
        f.writelines(content)


def main():
    parser = argparse.ArgumentParser(description='Add a filetype to the library.')  # noqa
    parser.add_argument('-m', '--mime',
                        required=True,
                        help='The mime type.')
    parser.add_argument('-e', '--extension',
                        required=True,
                        help='The extension name.')
    parser.add_argument('-s', '--signature',
                        nargs='+',
                        required=True,
                        help='The byte signature.')
    parser.add_argument('-t', '--type',
                        help='The type.')
    args = parser.parse_args()

    mime = args.mime
    extension = args.extension
    signature = [int(i, 16) for i in args.signature]
    type_ = args.type if args.type else mime.split('/')[0]
    classname = extension.capitalize()

    with open('add_filetype.j2') as f:
        template = Template(f.read())

    rendered = template.render(signature=signature,
                               mime=mime,
                               extension=extension,
                               classname=classname)

    path = os.path.join('filetype', 'types', '%s.py' % type_)
    if not os.path.exists(path):
        raise ValueError("Unknown type: '%s' try -t option." % type_)

    with open(path, 'a') as f:
        f.write('\n\n')
        f.write(rendered)

    with replace(os.path.join('filetype', 'types', '__init__.py')) as content:
        index = content.index('%s = (\n' % type_.upper())
        content.insert(index + 1, '    %s.%s(),\n' % (type_, classname))

    with replace('README.rst') as content:
        index = content.index('%s\n' % type_.capitalize())
        content.insert(index + 3, '-  **%s** - ``%s``\n' % (extension, mime))

    return 0


if __name__ == '__main__':
    sys.exit(main())
