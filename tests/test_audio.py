import io
import unittest

import filetype
from filetype.types.audio import Flac, Mp3


def id3_tag(version, size, footer=False):
    flags = 0x10 if footer else 0
    header = b'ID3' + bytes([version, 0, flags]) + bytes([
        (size >> 21) & 0x7f, (size >> 14) & 0x7f,
        (size >> 7) & 0x7f, size & 0x7f,
    ])
    return header + b'\0' * size + (b'3DI' + header[3:] if footer else b'')


class TestTaggedFlac(unittest.TestCase):
    def test_flac_after_id3(self):
        for version, size, footer in [(2, 0, False), (3, 2038, False), (4, 128, True)]:
            with self.subTest(version=version, size=size, footer=footer):
                data = id3_tag(version, size, footer) + b'fLaC'
                self.assertTrue(Flac().match(data))
                self.assertFalse(Mp3().match(data))
                for source in [data, bytearray(data), io.BytesIO(data)]:
                    self.assertEqual(filetype.guess_mime(source), 'audio/x-flac')
                    self.assertEqual(filetype.audio_match(source).extension, 'flac')

    def test_untagged_flac(self):
        self.assertEqual(filetype.guess_extension(b'fLaC'), 'flac')

    def test_mp3_after_id3(self):
        data = id3_tag(3, 128) + b'\xff\xfb\x00\x00'
        self.assertFalse(Flac().match(data))
        self.assertEqual(filetype.guess_extension(data), 'mp3')

    def test_flac_signature_inside_tag_is_not_audio(self):
        data = id3_tag(3, 4)[:10] + b'fLaC' + b'\xff\xfb\x00\x00'
        self.assertFalse(Flac().match(data))
        self.assertEqual(filetype.guess_extension(data), 'mp3')

    def test_truncated_or_invalid_tag_is_not_flac(self):
        for data in [
            b'', b'ID3', b'ID3\x04\x00\x00\x00\x00\x00',
            id3_tag(3, 128)[:10] + b'fLaC',
            b'ID3\x03\x00\x00\x80\x00\x00\x00fLaC',
            id3_tag(5, 0) + b'fLaC',
            id3_tag(4, 0, footer=True)[:-10] + b'fLaC',
        ]:
            with self.subTest(data=data):
                self.assertFalse(Flac().match(data))
