from __future__ import absolute_import

import io
import unittest

import filetype
from filetype.types.archive import Pdf


class TestPdf(unittest.TestCase):
    def test_leading_data(self):
        for prefix in (b'firmas_t/1082774737.png', b'<html></html>',
                       b'\x00' * 128, b' \r\n\t'):
            data = prefix + b'%PDF-1.7\n'
            for value in (data, bytearray(data), memoryview(data),
                          io.BytesIO(data)):
                kind = filetype.guess(value)
                self.assertIsNotNone(kind, repr(prefix))
                self.assertEqual(kind.extension, 'pdf')
                self.assertEqual(kind.mime, 'application/pdf')

    def test_header_search_is_bounded(self):
        matcher = Pdf()
        self.assertTrue(matcher.match(b'x' * 1019 + b'%PDF-1.7\n'))
        self.assertFalse(matcher.match(b'x' * 1020 + b'%PDF-1.7\n'))
        self.assertFalse(matcher.match(b'x' * 8192 + b'%PDF-1.7\n'))

    def test_existing_start_and_bom_signatures(self):
        for data in (b'%PDF', b'%PDF-1.7\n', b'\xef\xbb\xbf%PDF',
                     b'\xef\xbb\xbf%PDF-2.0\n'):
            self.assertTrue(Pdf().match(data))
            self.assertTrue(Pdf().match(bytearray(data)))

    def test_non_pdf_data(self):
        for data in (b'', b'%PD', b'prefix%PDF', b'prefix%PDX-1.7',
                     b'prefix%pdf-1.7', b'\x00' * 2048):
            self.assertFalse(Pdf().match(data), repr(data[:30]))

    def test_file_position_is_preserved(self):
        stream = io.BytesIO(b'leading data%PDF-1.7\n')
        stream.seek(4)
        self.assertEqual(filetype.guess_extension(stream), 'pdf')
        self.assertEqual(stream.tell(), 4)
