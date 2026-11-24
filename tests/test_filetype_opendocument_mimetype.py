import io
import struct
import unittest
import zipfile

import filetype


FORMATS = (
    ('application/vnd.oasis.opendocument.text', 'odt'),
    ('application/vnd.oasis.opendocument.spreadsheet', 'ods'),
    ('application/vnd.oasis.opendocument.presentation', 'odp'),
)


class StreamingOutput(io.BytesIO):
    def seekable(self):
        return False

    def seek(self, *args):
        raise io.UnsupportedOperation('seek')


def package(mime, streaming=False, filename='mimetype', extra=b'',
            compression=zipfile.ZIP_STORED):
    output = StreamingOutput() if streaming else io.BytesIO()
    info = zipfile.ZipInfo(filename)
    info.extra = extra
    info.compress_type = compression
    with zipfile.ZipFile(output, 'w') as archive:
        archive.writestr(info, mime.encode('ascii'))
    return output.getvalue()


class TestOpenDocumentMimetype(unittest.TestCase):
    def test_exact_mimetypes(self):
        for mime, extension in FORMATS:
            for streaming in (False, True):
                data = package(mime, streaming=streaming)
                self.assertEqual(filetype.guess_extension(data), extension)
                self.assertEqual(filetype.guess_mime(data), mime)

    def test_templates_are_not_documents(self):
        for mime, extension in FORMATS:
            for streaming in (False, True):
                data = package(mime + '-template', streaming=streaming)
                self.assertEqual(filetype.guess_extension(data), 'zip')

    def test_mime_text_in_a_filename_is_not_a_mimetype_entry(self):
        for mime, extension in FORMATS:
            data = package('unrelated', filename='mimetype' + mime)
            self.assertEqual(filetype.guess_extension(data), 'zip')

    def test_extra_field_is_skipped_before_the_payload(self):
        extra = b'\x55\x54\x05\x00\x01\x00\x00\x00\x00'
        for mime, extension in FORMATS:
            data = package(mime, extra=extra)
            self.assertEqual(filetype.guess_extension(data), extension)

    def test_unsigned_data_descriptor(self):
        for mime, extension in FORMATS:
            data = bytearray(package(mime, streaming=True))
            offset = data.index(b'PK\x07\x08')
            del data[offset:offset + 4]
            end = data.rindex(b'PK\x05\x06')
            directory = struct.unpack_from('<I', data, end + 16)[0]
            struct.pack_into('<I', data, end + 16, directory - 4)
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                self.assertEqual(archive.read('mimetype'),
                                 mime.encode('ascii'))
            self.assertEqual(filetype.guess_extension(data), extension)

    def test_compressed_mimetype_is_not_an_opendocument(self):
        for mime, extension in FORMATS:
            data = package(mime, compression=zipfile.ZIP_DEFLATED)
            self.assertEqual(filetype.guess_extension(data), 'zip')
