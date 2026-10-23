# -*- coding: utf-8 -*-

from __future__ import absolute_import

import io
import os
import struct
import unittest

import filetype

# Absolute path to fixtures directory
FIXTURES = os.path.dirname(os.path.abspath(__file__)) + '/fixtures'


class TestFileType(unittest.TestCase):
    def test_guess_jpeg(self):
        img_path = FIXTURES + '/sample.jpg'
        with open(img_path, 'rb') as fp:
            for obj in (img_path, fp):
                kind = filetype.guess(obj)
                self.assertTrue(kind is not None)
                self.assertEqual(kind.mime, 'image/jpeg')
                self.assertEqual(kind.extension, 'jpg')
            # reset reader position test
            kind = filetype.guess(fp)
            self.assertTrue(kind is not None)
            self.assertEqual(kind.mime, 'image/jpeg')
            self.assertEqual(kind.extension, 'jpg')

    def test_guess_jpx(self):
        kind = filetype.guess(FIXTURES + '/sample.jpx')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/jpx')
        self.assertEqual(kind.extension, 'jpx')

    def test_guess_jxl(self):
        kind = filetype.guess(FIXTURES + '/sample.jxl')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/jxl')
        self.assertEqual(kind.extension, 'jxl')

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

    def test_guess_avif(self):
        kind = filetype.guess(FIXTURES + '/sample.avif')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/avif')
        self.assertEqual(kind.extension, 'avif')

    def test_guess_dds(self):
        kind = filetype.guess(FIXTURES + '/sample.dds')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'image/dds')
        self.assertEqual(kind.extension, 'dds')

    def test_guess_m4a(self):
        kind = filetype.guess(FIXTURES + '/sample.m4a')
        self.assertTrue(kind is not None)
        self.assertEqual(kind.mime, 'audio/mp4')
        self.assertEqual(kind.extension, 'm4a')

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
        for name in 'sample.zst', 'sample_skippable.zst':
            kind = filetype.guess(FIXTURES + '/' + name)
            self.assertTrue(kind is not None)
            self.assertEqual(kind.mime, 'application/zstd')
            self.assertEqual(kind.extension, 'zst')

    def test_guess_doc(self):
        for name in 'sample.doc', 'sample_1.doc', 'sample_2.doc':
            kind = filetype.guess(os.path.join(FIXTURES, name))
            self.assertIsNotNone(kind)
            self.assertEqual(kind.mime, 'application/msword')
            self.assertEqual(kind.extension, 'doc')

    def test_guess_docx(self):
        for name in 'sample.docx', 'sample_1.docx':
            kind = filetype.guess(os.path.join(FIXTURES, name))
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


class TestBigTiff(unittest.TestCase):
    LITTLE_ENDIAN = b'II\x2b\x00\x08\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00'
    BIG_ENDIAN = b'MM\x00\x2b\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10'

    def assert_tiff(self, buf):
        kind = filetype.guess(buf)
        self.assertIsNotNone(kind)
        self.assertEqual(kind.extension, 'tif')
        self.assertEqual(kind.mime, 'image/tiff')
        self.assertEqual(filetype.guess_extension(buf), 'tif')
        self.assertEqual(filetype.guess_mime(buf), 'image/tiff')
        self.assertEqual(filetype.image_match(buf).extension, 'tif')
        self.assertTrue(filetype.is_image(buf))

    def header(self, endian, version=43, offset_size=8, reserved=0, first_ifd=16):
        return struct.pack(endian + '2sHHHQ', b'II' if endian == '<' else b'MM',
                           version, offset_size, reserved, first_ifd)

    def test_guess_little_endian_bigtiff(self):
        self.assert_tiff(self.LITTLE_ENDIAN)

    def test_guess_big_endian_bigtiff(self):
        self.assert_tiff(self.BIG_ENDIAN)

    def test_bigtiff_input_forms_are_preserved(self):
        for header in (self.LITTLE_ENDIAN, self.BIG_ENDIAN):
            buf = bytearray(header)
            self.assert_tiff(buf)
            self.assertEqual(buf, bytearray(header))
            self.assert_tiff(memoryview(header))
            stream = io.BytesIO(header)
            stream.seek(3)
            self.assert_tiff(stream)
            self.assertEqual(stream.tell(), 3)
            self.assertEqual(stream.getvalue(), header)

    def test_bigtiff_offset_bytes_are_not_a_cr2_marker(self):
        # A big-endian, aligned offset can start with CR in its high bytes.
        header = self.header('>', first_ifd=0x4352000000000010)
        self.assertEqual(header[8:10], b'CR')
        self.assert_tiff(header)

    def test_bigtiff_detection_does_not_validate_the_ifd_offset(self):
        # Detection identifies the header, without following or validating IFDs.
        for endian in ('<', '>'):
            for offset in (0, 16, 0xffffffffffffffff):
                self.assert_tiff(self.header(endian, first_ifd=offset))

    def test_bigtiff_requires_a_complete_header(self):
        for header in (self.LITTLE_ENDIAN, self.BIG_ENDIAN):
            for size in range(16):
                self.assertIsNone(filetype.guess(header[:size]))

    def test_bigtiff_rejects_wrong_versions(self):
        for endian in ('<', '>'):
            for version in (0, 41, 44, 0x2b00):
                self.assertIsNone(filetype.guess(self.header(endian, version=version)))

    def test_bigtiff_requires_eight_byte_offsets(self):
        for endian in ('<', '>'):
            for size in (0, 4, 16, 0x0800):
                self.assertIsNone(filetype.guess(self.header(endian, offset_size=size)))

    def test_bigtiff_requires_zero_reserved_bytes(self):
        for endian in ('<', '>'):
            for reserved in (1, 0x0100, 0xffff):
                self.assertIsNone(filetype.guess(self.header(endian, reserved=reserved)))

    def test_bigtiff_requires_consistent_byte_order(self):
        for marker in (b'IM', b'MI', b'ii', b'mm', b'MM'):
            self.assertIsNone(filetype.guess(marker + self.LITTLE_ENDIAN[2:]))
        self.assertIsNone(filetype.guess(b'II' + self.BIG_ENDIAN[2:]))

    def test_classic_tiff_and_cr2_are_preserved(self):
        for endian, marker in (('<', b'II'), ('>', b'MM')):
            classic = struct.pack(endian + '2sHI', marker, 42, 16) + b'\x00' * 8
            self.assert_tiff(classic)
            cr2 = classic[:8] + b'CR\x02\x00' + b'\x00' * 4
            self.assertEqual(filetype.guess_extension(cr2), 'cr2')
            self.assertEqual(filetype.guess_mime(cr2), 'image/x-canon-cr2')
