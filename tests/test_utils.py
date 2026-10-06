# -*- coding: utf-8 -*-


import unittest

import filetype
from filetype.utils import get_bytes


class TestMemoryviewSignature(unittest.TestCase):
    def test_signed_bytes_are_read_as_bytes(self):
        payload = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
        view = memoryview(payload).cast("b")
        self.assertEqual(get_bytes(view), payload)
        self.assertEqual(filetype.guess(view).extension, "png")

    def test_wide_elements_are_read_as_bytes(self):
        payload = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
        view = memoryview(payload).cast("H")
        self.assertEqual(get_bytes(view), payload)
        self.assertEqual(filetype.guess(view).extension, "png")

    def test_wide_elements_respect_byte_limit(self):
        payload = b"\x89PNG\r\n\x1a\n" + b"\x00" * 20000
        view = memoryview(payload).cast("H")
        self.assertEqual(get_bytes(view), payload[:8192])

    def test_strided_bytes_remain_supported(self):
        view = memoryview(b"abcdef")[::2]
        self.assertEqual(get_bytes(view), b"ace")
