# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

from collections import namedtuple

import filetype

import pytest

from . import FIXTURES


TestCase = namedtuple('NamedTuple', ['mime', 'buf', 'ext', 'filename'])


TEST_CASES = [
    TestCase('image/jpeg',
             [0xFF, 0xD8, 0xFF, 0x00, 0x08],
             'jpg',
             'sample.jpg'),
    TestCase('image/jpx',
             [],
             'jpx',
             'sample.jpx'),
    TestCase('image/png',
             [],
             'png',
             'sample.png'),
    TestCase('image/tiff',
             [],
             'tif',
             'sample.tif'),
    TestCase('image/gif',
             [],
             'gif',
             'sample.gif'),
    TestCase('image/heic',
             [],
             'heic',
             'sample.heic'),
    TestCase('video/mp4',
             [],
             'mp4',
             'sample.mp4'),
    TestCase('video/quicktime',
             [],
             'mov',
             'sample.mov'),
]


def name(test_data):
    return os.path.join(FIXTURES, test_data.filename)


def buf(test_data):
    if test_data.buf:
        return bytearray(test_data.buf)

    raise pytest.skip("No hex data defined for test case.")


def memview(test_data):
    return memoryview(buf(test_data))


@pytest.mark.parametrize('test_type', [name, buf, memview])
@pytest.mark.parametrize('test_data', TEST_CASES, ids=lambda x: x.mime)
def test_guess_kind(test_data, test_type):
    kind = filetype.guess(test_type(test_data))

    assert kind is not None
    assert kind.mime == test_data.mime
    assert kind.extension == test_data.ext


@pytest.mark.parametrize('test_type', [name, buf, memview])
@pytest.mark.parametrize('test_data', TEST_CASES, ids=lambda x: x.mime)
def test_guess_mime(test_data, test_type):
    mime = filetype.guess_mime(test_type(test_data))

    assert mime is not None
    assert mime == test_data.mime


@pytest.mark.parametrize('test_type', [name, buf, memview])
@pytest.mark.parametrize('test_data', TEST_CASES, ids=lambda x: x.mime)
def test_guess_extension(test_data, test_type):
    ext = filetype.guess_extension(test_type(test_data))

    assert ext is not None
    assert ext == test_data.ext


@pytest.mark.parametrize("bytes_",
                         [
                             [0xFF, 0x00, 0x00, 0x00, 0x00],
                         ])
def test_guess_invalid(bytes_):
    buf = bytearray(bytes_)

    kind = filetype.guess(buf)
    assert kind is None

    ext = filetype.guess_extension(buf)
    assert ext is None

    mime = filetype.guess_mime(buf)
    assert mime is None
