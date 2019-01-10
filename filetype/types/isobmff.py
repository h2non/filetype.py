# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import Type


class IsoBmff(Type):
    """
    Implements the ISO-BMFF base type.
    """
    def __init__(self, mime, extension):
        super(IsoBmff, self).__init__(
            mime=mime,
            extension=extension
        )

    def _is_isobmff(self, buf):
        if len(buf) < 16 or buf[4:8] != b'ftyp':
            return False
        if len(buf) < int.from_bytes(buf[0:4], byteorder='big'):
            return False
        return True

    def _get_ftyp(self, buf):
        ftyp_len = int.from_bytes(buf[0:4], byteorder='big')
        major_brand = buf[8:12].decode()
        minor_version = int.from_bytes(buf[12:16], byteorder='big')
        compatible_brands = []
        for i in range(16, ftyp_len, 4):
            compatible_brands.append(buf[i:i+4].decode())

        return major_brand, minor_version, compatible_brands
