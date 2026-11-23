# -*- coding: utf-8 -*-

import io
import os
import struct
import unittest

import filetype
from filetype.types.document import Doc, Ppt, Xls


NO_STREAM = 0xFFFFFFFF
END_OF_CHAIN = 0xFFFFFFFE


def entry(name, kind=2, left=NO_STREAM, right=NO_STREAM, child=NO_STREAM):
    """Build a directory entry; stream bodies are outside this header fixture."""
    result = bytearray(128)
    encoded = (name + '\0').encode('utf-16le')
    result[:len(encoded)] = encoded
    struct.pack_into('<HBBIII', result, 64, len(encoded), kind, 1,
                     left, right, child)
    return result


def header(entries, directory=3, continuation=None, version=3):
    """A bounded CFB header with the ambiguous FAT bytes reported in #205."""
    shift = 9 if version == 3 else 12
    sector_size = 1 << shift
    last = max(directory, continuation or 0)
    result = bytearray((last + 2) * sector_size)
    result[:8] = b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1'
    struct.pack_into('<HHHHH', result, 24, 0x3e, version, 0xfffe, shift, 6)
    struct.pack_into('<III', result, 40, 0 if version == 3 else 1, 1,
                     directory)
    struct.pack_into('<5I', result, 56, 4096, END_OF_CHAIN, 0,
                     END_OF_CHAIN, 0)
    struct.pack_into('<109I', result, 76, 1 if directory == 0 else 0,
                     *([NO_STREAM] * 108))
    if directory != 0:
        # FAT[0] is a FAT sector; FAT[1] points to 2 and FAT[2] ends a chain.
        # Consequently [518] == 0 but [522:524] == FF FF.
        struct.pack_into('<3I', result, sector_size, 0xfffffffd, 2,
                         END_OF_CHAIN)
        struct.pack_into('<I', result, sector_size + directory * 4,
                         continuation if continuation is not None else END_OF_CHAIN)
        if continuation is not None:
            struct.pack_into('<I', result, sector_size + continuation * 4,
                             END_OF_CHAIN)
    for index, value in enumerate(entries):
        page, slot = divmod(index, sector_size // 128)
        sector = directory if page == 0 else continuation
        offset = (sector + 1) * sector_size + slot * 128
        result[offset:offset + 128] = value
    return result


class TestLegacyOffice(unittest.TestCase):
    def test_shared_fat_signature_uses_powerpoint_directory(self):
        buf = header([entry('Root Entry', 5, child=1),
                      entry('PowerPoint Document')])
        self.assertEqual(buf[512:516], b'\xfd\xff\xff\xff')
        self.assertEqual(buf[518], 0)
        self.assertEqual(buf[522:524], b'\xff\xff')
        self.assertEqual(filetype.guess_extension(buf), 'ppt')
        self.assertEqual(filetype.guess_mime(buf), 'application/vnd.ms-powerpoint')
        self.assertTrue(Ppt().match(buf))
        self.assertFalse(Xls().match(buf))
        self.assertFalse(Doc().match(buf))

    def test_other_office_streams_keep_their_type(self):
        for name, extension in [('Workbook', 'xls'), ('Book', 'xls'),
                                ('WordDocument', 'doc')]:
            with self.subTest(name=name):
                buf = header([entry('Root Entry', 5, child=1), entry(name)])
                self.assertEqual(filetype.guess_extension(buf), extension)
                self.assertFalse(Ppt().match(buf))

    def test_buffers_and_seekable_streams(self):
        buf = header([entry('Root Entry', 5, child=1),
                      entry('PowerPoint Document')])
        for content in (buf, bytes(buf), memoryview(buf)):
            with self.subTest(type=type(content).__name__):
                self.assertEqual(filetype.guess_extension(content), 'ppt')
        stream = io.BytesIO(buf)
        stream.seek(17)
        self.assertEqual(filetype.guess_extension(stream), 'ppt')
        self.assertEqual(stream.tell(), 17)

    def test_directory_offset_and_noncontiguous_chain(self):
        buf = header([entry('Root Entry', 5, child=4), bytearray(128),
                      bytearray(128), bytearray(128),
                      entry('PowerPoint Document')], continuation=7)
        self.assertEqual(filetype.guess_extension(buf), 'ppt')

    def test_version_four_directory_in_header_window(self):
        buf = header([entry('Root Entry', 5, child=1),
                      entry('PowerPoint Document')], directory=0, version=4)
        self.assertEqual(filetype.guess_extension(buf), 'ppt')

    def test_nested_powerpoint_does_not_change_excel_container(self):
        buf = header([entry('Root Entry', 5, child=1),
                      entry('Objects', 1, right=3, child=2),
                      entry('PowerPoint Document'), entry('Workbook')])
        self.assertEqual(filetype.guess_extension(buf), 'xls')
        self.assertFalse(Ppt().match(buf))

    def test_unreachable_names_and_payload_strings_are_not_evidence(self):
        buf = header([entry('Root Entry', 5, child=1), entry('Workbook'),
                      entry('PowerPoint Document')])
        text = 'PowerPoint Document\0'.encode('utf-16le')
        buf[1024:1024 + len(text)] = text
        self.assertEqual(filetype.guess_extension(buf), 'xls')
        self.assertFalse(Ppt().match(buf))

    def test_never_reads_beyond_signature_limit(self):
        buf = header([entry('Root Entry', 5, child=1),
                      entry('PowerPoint Document')], directory=16)
        # With the directory outside the sniff window, retain the old heuristic.
        self.assertEqual(filetype.guess_extension(buf), 'xls')
        self.assertFalse(Ppt().match(buf))

    def test_malformed_directories_are_bounded_and_keep_legacy_fallback(self):
        root = entry('Root Entry', 5, child=1)
        for malformed in (entry('PowerPoint Document', left=1),
                          entry('PowerPoint Document', right=1000000),
                          entry('PowerPoint Document', kind=5)):
            with self.subTest(entry=bytes(malformed)):
                self.assertEqual(filetype.guess_extension(header([root, malformed])), 'xls')
        buf = header([root, entry('PowerPoint Document')])
        for length in (0, 7, 511, 512, 520, 2048, 2175, 2303):
            with self.subTest(length=length):
                self.assertNotEqual(filetype.guess_extension(buf[:length]), 'ppt')

    def test_existing_real_office_fixtures(self):
        fixtures = os.path.join(os.path.dirname(__file__), 'fixtures')
        for extension in ('doc', 'xls', 'ppt', 'docx', 'xlsx', 'pptx'):
            with self.subTest(extension=extension):
                path = os.path.join(fixtures, 'sample.' + extension)
                self.assertEqual(filetype.guess_extension(path), extension)

    def test_invalid_header_and_name_metadata_do_not_override_signatures(self):
        original = header([entry('Root Entry', 5, child=1),
                           entry('PowerPoint Document')])
        for offset, fmt, value in ((26, '<H', 1), (28, '<H', 0xfeff),
                                   (30, '<H', 16), (48, '<I', NO_STREAM),
                                   (2240, '<H', 65), (2240, '<H', 3),
                                   (2176, '<H', 0xd800)):
            with self.subTest(offset=offset, value=value):
                buf = bytearray(original)
                struct.pack_into(fmt, buf, offset, value)
                self.assertEqual(filetype.guess_extension(buf), 'xls')

    def test_cyclic_directory_sector_chain_is_bounded(self):
        buf = header([entry('Root Entry', 5, child=4), bytearray(128),
                      bytearray(128), bytearray(128),
                      entry('PowerPoint Document')], continuation=7)
        struct.pack_into('<I', buf, 512 + 3 * 4, 3)
        self.assertEqual(filetype.guess_extension(buf), 'xls')


if __name__ == '__main__':
    unittest.main()
