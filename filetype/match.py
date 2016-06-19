# -*- coding: utf-8 -*-

from filetype.types import types


def match(buf):
    """
    Performs bytes matching comparison agains the
    available type matchers.

    :param buf list
    :rtype bool
    """
    for matcher in types:
        if matcher.match(buf):
            return matcher

    return None