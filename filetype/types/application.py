# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import Type


class Wasm(Type):
    """
    Implements the WASM Web Assembly 1.0 filetype.

    WASM has starts with `\0asm`, followed by the version.
    http://webassembly.github.io/spec/core/binary/modules.html#binary-magic
    """

    MIME = 'application/wasm'
    EXTENSION = 'wasm'

    def __init__(self):
        super(Wasm, self).__init__(
            mime=Wasm.MIME,
            extension=Wasm.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 8 and
                buf[0] == 0x00 and
                buf[1] == 0x61 and
                buf[2] == 0x73 and
                buf[3] == 0x6D and
                buf[4] == 0x01 and
                buf[5] == 0x00 and
                buf[6] == 0x00 and
                buf[7] == 0x00)
