# -*- coding: utf-8 -*-

from filetype.match import match
from filetype.utils import get_signature_bytes


def guess_type(obj):
    """
    Infers the type of the given input.

    Function is overloaded to accept multiple types in input
    and peform the needed type inference based on it.

    :param obj str/list/bytes
    :rtype Type
    """
    if not obj:
        return None

    buf = None
    if type(obj) is bytes:
        buf = obj

    if type(obj) == str:
        buf = get_signature_bytes(obj)

    return match(buf)


def guess_mime(obj):
    """
    Infers the file type of the given input
    and returns its MIME type.

    :param obj str/list/bytes
    :rtype str
    """
    kind = guess_type(obj)
    return kind.mime if kind else kind


def guess_extension(obj):
    """
    Infers the file type of the given input
    and returns its RFC file extension.

    :param obj str/list/bytes
    :rtype str
    """
    kind = guess_type(obj)
    return kind.extension if kind else kind


def is_extension_supported(ext):
    return None


def is_extension_equals(ext):
    return None


def is_mime_supported(mime):
    return None


def is_mime_equals(mime):
    return None
