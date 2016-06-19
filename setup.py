#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

description = '''
Infer file type and MIME type of any file/buffer.
No libmagic dependency.
'''

config = {
    'name': 'filetype',
    'description': description,
    'author': 'Tomas Aparicio',
    'url': 'https://github.com/h2non/filetype.py',
    'download_url': 'https://github.com/h2non/filetype.py/tarball/master',
    'author_email': 'tomas@aparicio.me',
    'version': '0.1.0',
    'packages': ['filetype', 'filetype.types'],
    'scripts': [],
    'package_data': {
        'filetype': ['LICENSE', '*.md'],
    },
    'entry_points': {
        # 'console_scripts': [
        #   'filetype = filetype.cmd:run',
        # ],
    },
    'keywords': [
        'file',
        'libmagic',
        'magic',
        'infer',
        'numbers',
        'magicnumbers',
        'discovery',
        'mime',
        'type',
        'kind',
    ],
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
        'Operating System :: OS Independent'
    ],
}

setup(**config)
