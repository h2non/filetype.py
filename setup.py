#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
# To use a consistent encoding

description = '''
Infer file type and MIME type of any file/buffer.
No libmagic dependency.
'''


config = {
    'name': 'filetype',
    'description': description,
    'author': 'Tomas Aparicio',
    'author_email': 'tomas@aparicio.me',
    'url': 'https://github.com/h2non/filetype.py',
    'download_url': 'https://github.com/h2non/filetype.py/tarball/master',
    'version': '0.1.3',
    'license': 'MIT',
    'packages': find_packages(exclude=['dist', 'build', 'docs', 'tests']),
    'package_data': {
        'filetype': ['LICENSE', '*.md'],
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
        'Programming Language :: Python :: 3.6',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
        'Operating System :: OS Independent'
    ],
}

setup(**config)
