import unittest

import filetype
from filetype.match import image_match, match
from filetype.types.image import Dcm, Tiff


class TestDicomPreamble(unittest.TestCase):
    def test_dicom_takes_precedence_over_preamble_signatures(self):
        # PS3.10 permits other image formats in the 128-byte preamble.
        for prefix in (b'II\x2a\x00', b'MM\x00\x2a', b'\xff\xd8\xff',
                       b'BM', b'AC10', b''):
            data = prefix.ljust(128, b'\x00') + b'DICM\x02\x00'
            for buffer_type in (bytes, bytearray):
                with self.subTest(prefix=prefix, buffer_type=buffer_type):
                    buf = buffer_type(data)
                    self.assertEqual(filetype.guess_mime(buf),
                                     'application/dicom')
                    self.assertEqual(filetype.guess_extension(buf), 'dcm')
                    self.assertIsInstance(image_match(buf), Dcm)

    def test_tiff_without_dicom_prefix(self):
        for prefix in (b'II\x2a\x00', b'MM\x00\x2a'):
            for suffix in (b'', b'DIC', b'DICX\x02\x00'):
                with self.subTest(prefix=prefix, suffix=suffix):
                    data = prefix.ljust(128, b'\x00') + suffix
                    self.assertIsInstance(filetype.guess(data), Tiff)
                    self.assertIsInstance(image_match(data), Tiff)

    def test_explicit_matcher_order_is_respected(self):
        data = b'II\x2a\x00'.ljust(128, b'\x00') + b'DICM\x02\x00'
        self.assertIsInstance(match(data, [Tiff(), Dcm()]), Tiff)
