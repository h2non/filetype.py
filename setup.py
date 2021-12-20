#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from setuptools import find_packages, setup

setup(
    name='filetype',
    version='1.0.9',
    description='Infer file type and MIME type of any file/buffer. '
                'No external dependencies.',
    long_description=codecs.open('README.rst', 'r',
                                 encoding='utf-8', errors='ignore').read(),
    keywords='file libmagic magic infer numbers magicnumbers discovery mime '
             'type kind',
    url='https://github.com/h2non/filetype.py',
    download_url='https://github.com/h2non/filetype.py/tarball/master',
    author='Tomas Aparicio',
    author_email='tomas@aparicio.me',
    license='MIT',
    license_files=['LICENSE'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: System',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities'],
    platforms=['any'],
    packages=find_packages(exclude=['dist', 'build', 'docs', 'tests',
                                    'examples']),
    package_data={'filetype': ['LICENSE', '*.md']},
    zip_safe=True,
    entry_points={
        'console_scripts': ['filetype=filetype.__main__:main'],
    })
