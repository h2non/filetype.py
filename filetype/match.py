# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .types import ARCHIVE as archive_matchers
from .types import AUDIO as audio_matchers
from .types import FONT as font_matchers
from .types import IMAGE as image_matchers
from .types import VIDEO as video_matchers
from .types import TYPES
from .utils import get_bytes


def match(obj, matchers=TYPES):
    """
    Matches the given input againts the available
    file type matchers.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        Type instance if type matches. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    buf = get_bytes(obj)

    for matcher in matchers:
        if matcher.match(buf):
            return matcher

    return None


def image(obj):
    """
    Matches the given input againts the available
    image type matchers.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        Type instance if matches. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match(obj, image_matchers)


def font(obj):
    """
    Matches the given input againts the available
    font type matchers.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        Type instance if matches. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match(obj, font_matchers)


def video(obj):
    """
    Matches the given input againts the available
    video type matchers.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        Type instance if matches. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match(obj, video_matchers)


def audio(obj):
    """
    Matches the given input againts the available
    autio type matchers.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        Type instance if matches. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match(obj, audio_matchers)


def archive(obj):
    """
    Matches the given input againts the available
    archive type matchers.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        Type instance if matches. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match(obj, archive_matchers)
