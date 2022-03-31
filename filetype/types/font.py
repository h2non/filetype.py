# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import Type


class Woff(Type):
    """
    Implements the WOFF font type matcher.
    """
    MIME = 'application/font-woff'
    EXTENSION = 'woff'

    def __init__(self):
        super(Woff, self).__init__(
            mime=Woff.MIME,
            extension=Woff.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x77 and
                buf[1] == 0x4F and
                buf[2] == 0x46 and
                buf[3] == 0x46)


class Woff2(Type):
    """
    Implements the WOFF2 font type matcher.
    """
    MIME = 'application/font-woff'
    EXTENSION = 'woff2'

    def __init__(self):
        super(Woff2, self).__init__(
            mime=Woff2.MIME,
            extension=Woff2.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 3 and
                buf[0] == 0x77 and
                buf[1] == 0x4F and
                buf[2] == 0x46 and
                buf[3] == 0x32)


class Ttf(Type):
    """
    Implements the TTF font type matcher.
    """
    MIME = 'application/font-sfnt'
    EXTENSION = 'ttf'

    def __init__(self):
        super(Ttf, self).__init__(
            mime=Ttf.MIME,
            extension=Ttf.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x00 and
                buf[1] == 0x01 and
                buf[2] == 0x00 and
                buf[3] == 0x00 and
                buf[4] == 0x00)


class Otf(Type):
    """
    Implements the OTF font type matcher.
    """
    MIME = 'application/font-sfnt'
    EXTENSION = 'otf'

    def __init__(self):
        super(Otf, self).__init__(
            mime=Otf.MIME,
            extension=Otf.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 4 and
                buf[0] == 0x4F and
                buf[1] == 0x54 and
                buf[2] == 0x54 and
                buf[3] == 0x4F and
                buf[4] == 0x00)
