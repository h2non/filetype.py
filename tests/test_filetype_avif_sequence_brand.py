import struct
import unittest

import filetype
from filetype.types.image import Avif


def ftyp(major, compatible):
    payload = major + b'\0\0\0\0' + b''.join(compatible)
    return struct.pack('>I', len(payload) + 8) + b'ftyp' + payload


class TestAvifSequenceBrand(unittest.TestCase):
    def test_sequence_compatible_brand(self):
        for major in (b'msf1', b'mif1'):
            for brands in ([b'avis'], [b'msf1', b'avis'], [b'avis', b'msf1']):
                data = ftyp(major, brands)
                self.assertEqual(filetype.guess_extension(data), 'avif')
                self.assertEqual(filetype.guess_mime(data), 'image/avif')

    def test_existing_still_and_sequence_brands(self):
        for major, compatible in ((b'avif', []), (b'avis', []),
                                  (b'mif1', [b'avif'])):
            self.assertEqual(filetype.guess_extension(ftyp(major, compatible)),
                             'avif')

    def test_unrelated_compatible_brands(self):
        for brands in ([], [b'msf1'], [b'av01'], [b'heic']):
            self.assertFalse(Avif().match(ftyp(b'msf1', brands)))
