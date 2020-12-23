# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

import filetype

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
