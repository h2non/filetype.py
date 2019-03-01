# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import unittest

import filetype

# Absolute path to fixtures directory
FIXTURES = os.path.dirname(os.path.abspath(__file__)) + '/fixtures'


class TestFileType(unittest.TestCase):
    def test_guess_jpeg(self):
        kind = filetype.guess(FIXTURES + '/sample.jpg')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/jpeg')
        self.assertEqual(kind.extension, 'jpg')

    def test_guess_jpx(self):
        kind = filetype.guess(FIXTURES + '/sample.jpx')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/jpx')
        self.assertEqual(kind.extension, 'jpx')

    def test_guess_gif(self):
        kind = filetype.guess(FIXTURES + '/sample.gif')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/gif')
        self.assertEqual(kind.extension, 'gif')

    def test_guess_heic(self):
        kind = filetype.guess(FIXTURES + '/sample.heic')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/heic')
        self.assertEqual(kind.extension, 'heic')

    def test_guess_mp4(self):
        kind = filetype.guess(FIXTURES + '/sample.mp4')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'video/mp4')
        self.assertEqual(kind.extension, 'mp4')

    def test_guess_png(self):
        kind = filetype.guess(FIXTURES + '/sample.png')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/png')
        self.assertEqual(kind.extension, 'png')

    def test_guess_tif(self):
        kind = filetype.guess(FIXTURES + '/sample.tif')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/tiff')
        self.assertEqual(kind.extension, 'tif')

    def test_guess_mov(self):
        kind = filetype.guess(FIXTURES + '/sample.mov')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'video/quicktime')
        self.assertEqual(kind.extension, 'mov')
