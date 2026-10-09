# -*- coding: utf-8 -*-

import io
import os
import unittest

import filetype
from filetype.utils import get_bytes


class NonSeekableStream(io.RawIOBase):
    def __init__(self, data):
        self.data = io.BytesIO(data)

    def read(self, size=-1):
        return self.data.read(size)


class TestFileLikeInputs(unittest.TestCase):
    def test_guess_pipe(self):
        read_fd, write_fd = os.pipe()
        with os.fdopen(read_fd, 'rb') as reader:
            with os.fdopen(write_fd, 'wb') as writer:
                writer.write(b'%PDF-1.7\n')
            self.assertEqual(filetype.guess_extension(reader), 'pdf')

    def test_non_seekable_read_is_bounded(self):
        stream = NonSeekableStream(b'a' * 8192 + b'remaining')
        self.assertEqual(get_bytes(stream), b'a' * 8192)
        self.assertEqual(stream.read(), b'remaining')

    def test_seekable_position_is_preserved(self):
        stream = io.BytesIO(b'%PDF-1.7\nbody')
        stream.seek(5)
        self.assertEqual(filetype.guess_extension(stream), 'pdf')
        self.assertEqual(stream.tell(), 5)
