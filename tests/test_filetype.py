# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import unittest

import filetype

# Absolute path to fixtures directory
FIXTURES = os.path.dirname(os.path.abspath(__file__)) + '/fixtures'


class TestFileType(unittest.TestCase):
    def test_guess_file_path(self):
        kind = filetype.guess(FIXTURES + '/sample.jpg')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/jpeg')
        self.assertEqual(kind.extension, 'jpg')

    def test_guess_buffer(self):
        buf = bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08])
        kind = filetype.guess(buf)
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/jpeg')
        self.assertEqual(kind.extension, 'jpg')

    def test_guess_buffer_invalid(self):
        buf = bytearray([0xFF, 0x00, 0x00, 0x00, 0x00])
        kind = filetype.guess(buf)
        self.assertTrue(kind is None)

    def test_guess_memoryview(self):
        buf = memoryview(bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08]))
        kind = filetype.guess(buf)
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/jpeg')
        self.assertEqual(kind.extension, 'jpg')


class TestFileTypeExtension(unittest.TestCase):
    def test_guess_extension_file_path(self):
        ext = filetype.guess_extension(FIXTURES + '/sample.jpg')
        self.assertTrue(ext is not None)
        self.assertEqual(ext, 'jpg')

    def test_guess_extension_buffer(self):
        buf = bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08])
        ext = filetype.guess_extension(buf)
        self.assertTrue(ext is not None)
        self.assertEqual(ext, 'jpg')

    def test_guess_extension_buffer_invalid(self):
        buf = bytearray([0xFF, 0x00, 0x00, 0x00, 0x00])
        ext = filetype.guess_extension(buf)
        self.assertTrue(ext is None)

    def test_guess_extension_memoryview(self):
        buf = memoryview(bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08]))
        ext = filetype.guess_extension(buf)
        self.assertTrue(ext is not None)
        self.assertEqual(ext, 'jpg')


class TestFileTypeMIME(unittest.TestCase):
    def test_guess_mime_file_path(self):
        mime = filetype.guess_mime(FIXTURES + '/sample.jpg')
        self.assertTrue(mime is not None)
        self.assertEqual(mime, 'image/jpeg')

    def test_guess_mime_buffer(self):
        buf = bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08])
        mime = filetype.guess_mime(buf)
        self.assertTrue(mime is not None)
        self.assertEqual(mime, 'image/jpeg')

    def test_guess_mime_buffer_invalid(self):
        buf = bytearray([0xFF, 0x00, 0x00, 0x00, 0x00])
        mime = filetype.guess_mime(buf)
        self.assertTrue(mime is None)

    def test_guess_mime_memoryview(self):
        buf = memoryview(bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08]))
        mime = filetype.guess_mime(buf)
        self.assertTrue(mime is not None)
        self.assertEqual(mime, 'image/jpeg')
