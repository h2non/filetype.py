# -*- coding: utf-8 -*-

import io
import os
import unittest

import filetype


class TestSvg(unittest.TestCase):
    def assert_svg(self, data):
        kind = filetype.guess(data)
        self.assertIsNotNone(kind)
        self.assertEqual(kind.extension, 'svg')
        self.assertEqual(kind.mime, 'image/svg+xml')
        self.assertTrue(filetype.is_image(data))

    def test_root_forms(self):
        for data in (
            b'<svg/>',
            b' \n<svg xmlns="http://www.w3.org/2000/svg"/>',
            b'<s:svg xmlns:s="http://www.w3.org/2000/svg"/>',
            b'<?xml version="1.0"?><svg width="10" height="20"/>',
            b'<!-- <html> is only a comment -->\n<svg/>',
            b'<?xml-stylesheet href="style.css" type="text/css"?><svg/>',
            b'<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
            b'"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"><svg/>',
        ):
            with self.subTest(data=data):
                self.assert_svg(data)

    def test_unicode_encodings(self):
        source = '<svg xmlns="http://www.w3.org/2000/svg"><title>image</title></svg>'
        for data in (
            source.encode('utf-8-sig'),
            source.encode('utf-16'),
            b'\xfe\xff' + source.encode('utf-16-be'),
        ):
            with self.subTest(data=data[:4]):
                self.assert_svg(data)

    def test_file_and_binary_input_forms(self):
        filename = os.path.join(os.path.dirname(__file__), 'fixtures', 'sample.svg')
        with open(filename, 'rb') as stream:
            data = stream.read()
            stream.seek(7)
            self.assert_svg(stream)
            self.assertEqual(stream.tell(), 7)
        for value in (filename, data, bytearray(data), memoryview(data), io.BytesIO(data)):
            with self.subTest(input_type=type(value).__name__):
                self.assert_svg(value)

    def test_helpers_use_registered_svg_type(self):
        self.assertEqual(filetype.guess_extension(b'<svg/>'), 'svg')
        self.assertEqual(filetype.guess_mime(b'<svg/>'), 'image/svg+xml')
        self.assertEqual(filetype.get_type(ext='svg').mime, 'image/svg+xml')

    def test_other_xml_and_embedded_svg_do_not_match(self):
        for data in (
            b'<html><svg/></html>',
            b'<document><svg/></document>',
            b'<svg-preview/>',
            b'<SVG/>',
            b'<svg xmlns="urn:unrelated"/>',
            b'<!-- <svg/> --><document/>',
            b'plain text mentioning <svg/>',
            b'<![CDATA[<svg/>]]>',
            b'<svg',
            b'<svg xmlns="unfinished',
            b'<?xml version="1.0" encoding="unknown-encoding"?><svg/>',
        ):
            with self.subTest(data=data):
                self.assertIsNone(filetype.guess(data))

    def test_entity_declarations_are_not_expanded(self):
        for declaration in (
            b'<!ENTITY label "image">',
            b'<!ENTITY label SYSTEM "file:///does-not-exist">',
            b'<!ENTITY % external SYSTEM "https://example.com/external.dtd">%external;',
        ):
            with self.subTest(declaration=declaration):
                data = b'<!DOCTYPE svg [' + declaration + b']><svg/>'
                self.assertIsNone(filetype.guess(data))

    def test_only_the_header_is_needed(self):
        # Like other signatures, identifying the root does not validate the body.
        self.assert_svg(b'<svg xmlns="http://www.w3.org/2000/svg">' + b' ' * 10000)

    def test_root_must_be_within_the_header_read_limit(self):
        self.assertIsNone(filetype.guess(b'<!--' + b' ' * 8192 + b'--><svg/>'))
