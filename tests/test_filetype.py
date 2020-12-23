# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys

# Python 2.7 workaround
try:
    import pathlib
except ImportError:
    pathlib = None

import filetype
from filetype.types import image
from filetype.types.base import Type

import pytest

from . import FIXTURES


class TestFileType(object):

    def test_guess_file_path(self):
        kind = filetype.guess(os.path.join(FIXTURES, 'sample.jpg'))
        assert kind is not None
        assert kind.mime == 'image/jpeg'
        assert kind.extension == 'jpg'

    def test_guess_buffer(self):
        buf = bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08])
        kind = filetype.guess(buf)
        assert kind is not None
        assert kind.mime == 'image/jpeg'
        assert kind.extension == 'jpg'

    def test_guess_buffer_invalid(self):
        buf = bytearray([0xFF, 0x00, 0x00, 0x00, 0x00])
        kind = filetype.guess(buf)
        assert kind is None

    def test_guess_memoryview(self):
        buf = memoryview(bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08]))
        kind = filetype.guess(buf)
        assert kind is not None
        assert kind.mime == 'image/jpeg'
        assert kind.extension == 'jpg'

    @pytest.mark.skipif(sys.version_info < (3,),
                        reason="No workarounds anymore for python 2.7")
    def test_guess_bytes(self):
        buf = bytes(bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08]))
        kind = filetype.guess(buf)
        assert kind is not None
        assert kind.mime == 'image/jpeg'
        assert kind.extension == 'jpg'

    @pytest.mark.skipif(sys.version_info < (3, 6),
                        reason="No workarounds for unsupported versions")
    def test_guess_pathlib(self):
        path = pathlib.Path(os.path.join(FIXTURES, 'sample.jpg'))
        kind = filetype.guess(path)
        assert kind is not None
        assert kind.mime == 'image/jpeg'
        assert kind.extension == 'jpg'

    @pytest.mark.skipif(sys.version_info < (3, 6),
                        reason="No workarounds for unsupported versions")
    def test_invalid_input(self):
        with pytest.raises(TypeError):
            filetype.guess(tuple)


class TestFileTypeExtension(object):

    def test_guess_extension_file_path(self):
        ext = filetype.guess_extension(os.path.join(FIXTURES, 'sample.jpg'))
        assert ext is not None
        assert ext == 'jpg'

    def test_guess_extension_buffer(self):
        buf = bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08])
        ext = filetype.guess_extension(buf)
        assert ext is not None
        assert ext == 'jpg'

    def test_guess_extension_buffer_invalid(self):
        buf = bytearray([0xFF, 0x00, 0x00, 0x00, 0x00])
        ext = filetype.guess_extension(buf)
        assert ext is None

    def test_guess_extension_memoryview(self):
        buf = memoryview(bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08]))
        ext = filetype.guess_extension(buf)
        assert ext is not None
        assert ext == 'jpg'


class TestFileTypeMIME(object):

    def test_guess_mime_file_path(self):
        mime = filetype.guess_mime(os.path.join(FIXTURES, 'sample.jpg'))
        assert mime is not None
        assert mime == 'image/jpeg'

    def test_guess_mime_buffer(self):
        buf = bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08])
        mime = filetype.guess_mime(buf)
        assert mime is not None
        assert mime == 'image/jpeg'

    def test_guess_mime_buffer_invalid(self):
        buf = bytearray([0xFF, 0x00, 0x00, 0x00, 0x00])
        mime = filetype.guess_mime(buf)
        assert mime is None

    def test_guess_mime_memoryview(self):
        buf = memoryview(bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08]))
        mime = filetype.guess_mime(buf)
        assert mime is not None
        assert mime == 'image/jpeg'


def test_get_type_mime():
    type_ = filetype.get_type(mime='image/png')
    assert isinstance(type_, image.Png)


def test_get_type_ext():
    type_ = filetype.get_type(ext='png')
    assert isinstance(type_, image.Png)


def test_get_type():
    type_ = filetype.get_type(mime='image/png', ext='png')
    assert isinstance(type_, image.Png)


def test_get_type_invalid():
    type_ = filetype.get_type(mime='foo', ext='bar')
    assert type_ is None


def test_invalid_custom_type():
    with pytest.raises(TypeError):
        filetype.add_type(tuple)


@pytest.mark.skipif(sys.version_info < (3,),
                    reason="No workarounds anymore for python 2.7")
def test_custom_type():
    mime = 'app/bar'
    ext = 'bar'

    class Custom(Type):

        def __init__(self):
            super().__init__(mime=mime, extension=ext)

        def match(self, buf):
            return buf == b"bar"

    filetype.add_type(Custom())
    kind = filetype.guess(b"bar")

    assert kind.extension == ext
    assert kind.mime == mime
