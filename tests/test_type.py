# -*- coding: utf-8 -*-

import unittest

from filetype.types.image import Png


class TestType(unittest.TestCase):
    def test_is_extension_compares_string_values(self):
        extension = ''.join(['p', 'n', 'g'])
        self.assertTrue(Png().is_extension(extension))

    def test_is_mime_compares_string_values(self):
        mime = ''.join(['image/', 'png'])
        self.assertTrue(Png().is_mime(mime))

    def test_is_extension_rejects_different_values(self):
        self.assertFalse(Png().is_extension('jpg'))
        self.assertFalse(Png().is_extension('PNG'))
        self.assertFalse(Png().is_extension(None))

    def test_is_mime_rejects_different_values(self):
        self.assertFalse(Png().is_mime('image/jpeg'))
        self.assertFalse(Png().is_mime('image/PNG'))
        self.assertFalse(Png().is_mime(None))
