import struct
import unittest

import filetype
from filetype.types.video import M4v


def ftyp(brand, compatible):
    payload = brand + b'\0\0\0\0' + b''.join(compatible)
    return struct.pack('>I', 8 + len(payload)) + b'ftyp' + payload


class TestM4vBoxSize(unittest.TestCase):
    def test_variable_compatible_brand_count(self):
        for count in range(1, 6):
            data = ftyp(b'M4V ', [b'M4V '] * count)
            self.assertEqual(filetype.guess_extension(data), 'm4v')
            self.assertEqual(filetype.guess_mime(data), 'video/x-m4v')

    def test_existing_major_brand_variants(self):
        for brand in (b'M4V ', b'M4VH', b'M4VP'):
            self.assertEqual(filetype.guess_extension(ftyp(brand, [brand])),
                             'm4v')

    def test_truncated_file_type_box(self):
        data = ftyp(b'M4V ', [b'M4V '])
        for end in range(len(data)):
            self.assertFalse(M4v().match(data[:end]))

    def test_other_brands(self):
        for brand, extension in ((b'mp42', 'mp4'), (b'qt  ', 'mov'),
                                 (b'M4A ', 'm4a')):
            data = ftyp(brand, [brand])
            self.assertFalse(M4v().match(data))
            self.assertEqual(filetype.guess_extension(data), extension)
