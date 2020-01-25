# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import Type


class Doc(Type):
    """
    Implements Doc file type matcher.
    """

    MIME = 'application/msword'
    EXTENSION = 'doc'

    def __init__(self):
        super(Doc, self).__init__(
            mime=Doc.MIME,
            extension=Doc.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 7 and
                buf[0] == 0xD0 and
                buf[1] == 0xCF and
                buf[2] == 0x11 and
                buf[3] == 0xE0 and
                buf[4] == 0xA1 and
                buf[5] == 0xB1 and
                buf[6] == 0x1A and
                buf[7] == 0xE1)


# todo: Docx


class Xls(Type):
    """
    Implements Xls file type matcher.
    Which looks like the Doc file type matcher..
    """

    MIME = 'application/vnd.ms-excel'
    EXTENSION = 'xls'

    def __init__(self):
        super(Xls, self).__init__(
            mime=Xls.MIME,
            extension=Xls.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 7 and
                buf[0] == 0xD0 and
                buf[1] == 0xCF and
                buf[2] == 0x11 and
                buf[3] == 0xE0 and
                buf[4] == 0xA1 and
                buf[5] == 0xB1 and
                buf[6] == 0x1A and
                buf[7] == 0xE1)


# todo: Xlsx


class Ppt(Type):
    """
    Implements Ppt file type matcher.
    Which looks like the Doc and Xls file type matchers..
    """

    MIME = 'application/vnd.ms-powerpoint'
    EXTENSION = 'ppt'

    def __init__(self):
        super(Ppt, self).__init__(
            mime=Ppt.MIME,
            extension=Ppt.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 7 and
                buf[0] == 0xD0 and
                buf[1] == 0xCF and
                buf[2] == 0x11 and
                buf[3] == 0xE0 and
                buf[4] == 0xA1 and
                buf[5] == 0xB1 and
                buf[6] == 0x1A and
                buf[7] == 0xE1)
