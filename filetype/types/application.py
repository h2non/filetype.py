# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import Type


class Wasm(Type):
    """Implements the Wasm image type matcher."""

    MIME = 'application/wasm'
    EXTENSION = 'wasm'

    def __init__(self):
        super(Wasm, self).__init__(
            mime=Wasm.MIME,
            extension=Wasm.EXTENSION
        )

    def match(self, buf):
        return buf[:8] == bytearray([0x00, 0x61, 0x73, 0x6d,
                                     0x01, 0x00, 0x00, 0x00])


class Parquet(Type):
    """Implements the Apache Parquet type matcher."""

    MIME = 'application/vnd.apache.parquet'
    EXTENSION = 'parquet'

    def __init__(self):
        super(Parquet, self).__init__(
            mime=Parquet.MIME,
            extension=Parquet.EXTENSION
        )

    def match(self, buf):
        return buf[:4] == bytearray([0x50, 0x41, 0x52, 0x31])
