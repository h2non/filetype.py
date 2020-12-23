# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import filetype

import pytest

from . import FIXTURES


@pytest.mark.parametrize('filename',
                         [
                             'sample.jpg',
                             'sample.mp4',
                             'sample.zip',
                             'sample.tar',
                         ])
def test_infer_from_disk(benchmark, filename):
    benchmark(filetype.guess, os.path.join(FIXTURES, filename))


@pytest.mark.parametrize('bytes_',
                         [
                             [0xFF, 0xD8, 0xFF, 0x00, 0x08],
                             [0x1A, 0x45, 0xDF, 0xA3, 0x08],
                             [0x4D, 0x54, 0x68, 0xA3, 0x64],
                         ],
                         ids=['image', 'video', 'audio'])
def test_infer_from_bytes(benchmark, bytes_):
    benchmark(filetype.guess, bytearray(bytes_))
