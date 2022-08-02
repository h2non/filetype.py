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

    def test_guess_zstd(self):
        kind = filetype.guess(FIXTURES + '/sample.zst')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/zstd')
        self.assertEqual(kind.extension, 'zst')

    def test_guess_doc(self):
        kind = filetype.guess(FIXTURES + '/sample.doc')
        self.assertIsNotNone(kind)
        self.assertEqual(kind.mime, 'application/msword')
        self.assertEqual(kind.extension, 'doc')

    def test_guess_docx(self):
        kind = filetype.guess(FIXTURES + '/sample.docx')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        self.assertEqual(kind.extension, 'docx')

    def test_guess_odt(self):
        kind = filetype.guess(FIXTURES + '/sample.odt')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/vnd.oasis.opendocument.text')
        self.assertEqual(kind.extension, 'odt')    
        
    def test_guess_xls(self):
        kind = filetype.guess(FIXTURES + '/sample.xls')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/vnd.ms-excel')
        self.assertEqual(kind.extension, 'xls')

    def test_guess_xlsx(self):
        kind = filetype.guess(FIXTURES + '/sample.xlsx')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        self.assertEqual(kind.extension, 'xlsx')

    def test_guess_ods(self):
        kind = filetype.guess(FIXTURES + '/sample.ods')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/vnd.oasis.opendocument.spreadsheet')
        self.assertEqual(kind.extension, 'ods') 

    def test_guess_ppt(self):
        kind = filetype.guess(FIXTURES + '/sample.ppt')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/vnd.ms-powerpoint')
        self.assertEqual(kind.extension, 'ppt')

    def test_guess_pptx(self):
        kind = filetype.guess(FIXTURES + '/sample.pptx')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/vnd.openxmlformats-officedocument.presentationml.presentation')
        self.assertEqual(kind.extension, 'pptx')

    def test_guess_odp(self):
        kind = filetype.guess(FIXTURES + '/sample.odp')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'application/vnd.oasis.opendocument.presentation')
        self.assertEqual(kind.extension, 'odp') 