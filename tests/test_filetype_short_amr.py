import unittest

import filetype
from filetype.types.audio import Amr


class TestShortAmr(unittest.TestCase):
    def test_single_no_data_frame(self):
        # RFC 4867 storage header, followed by FT=15, Q=1 (NO_DATA).
        data = b'#!AMR\n\x7c'
        for value in (data, bytearray(data)):
            kind = filetype.guess(value)
            self.assertIsNotNone(kind)
            self.assertEqual(kind.extension, 'amr')
            self.assertEqual(kind.mime, 'audio/amr')

    def test_all_truncated_headers(self):
        header = b'#!AMR\n'
        for end in range(len(header)):
            self.assertFalse(Amr().match(header[:end]))

    def test_other_headers_do_not_match(self):
        for data in (b'#!AMR-WB\n\x7c', b'#!AMX\n\x7c', b'#!AMR\r\n\x7c'):
            self.assertFalse(Amr().match(data))
