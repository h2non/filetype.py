# -*- coding: utf-8 -*-

from __future__ import absolute_import

from os import PathLike

from .match import match
from .types import TYPES, Type

# Expose supported matchers types
types = TYPES


def guess(obj):
    """
    Infers the type of the given input.

    Function is overloaded to accept multiple types in input
    and perform the needed type inference based on it.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        The matched type instance. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    return match(obj) if obj else None


def guess_mime(obj):
    """
    Infers the file type of the given input
    and returns its MIME type.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        The matched MIME type as string. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    kind = guess(obj)
    return kind.mime if kind else kind


def guess_extension(obj):
    """
    Infers the file type of the given input
    and returns its RFC file extension.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        The matched file extension as string. Otherwise None.

    Raises:
        TypeError: if obj is not a supported type.
    """
    kind = guess(obj)
    return kind.extension if kind else kind


def get_type(mime=None, ext=None):
    """
    Returns the file type instance searching by
    MIME type or file extension.

    Args:
        ext: file extension string. E.g: jpg, png, mp4, mp3
        mime: MIME string. E.g: image/jpeg, video/mpeg

    Returns:
        The matched file type instance. Otherwise None.
    """
    for kind in types:
        if kind.extension == ext or kind.mime == mime:
            return kind
    return None


def add_type(instance):
    """
    Adds a new type matcher instance to the supported types.

    Args:
        instance: Type inherited instance.

    Returns:
        None
    """
    if not isinstance(instance, Type):
        raise TypeError('instance must inherit from filetype.types.Type')

    types.insert(0, instance)


# Convert filetype extensions to imghdr extensions
imghdr_exts = {"jpg": "jpeg", "tif": "tiff"}


def what(file: PathLike | str | None, h: bytes | None) -> str:
    """A drop-in replacement for `imghdr.what()` which was removed from the standard
    library in Python 3.13.

    Usage:
    ```python
    # Replace...
    from imghdr import what
    # with...
    from filetype import what
    # ---
    # Or replace...
    import imghdr
    ext = imghdr.what(...)
    # with...
    import filetype
    ext = filetype.what(...)
    ```

    imghdr documentation: https://docs.python.org/3.12/library/imghdr.html
    imghdr source code: https://github.com/python/cpython/blob/3.12/Lib/imghdr.py
    """
    image_type = guess(h) if h else guess(file)
    ext = str(image_type) if image_type else None
    return imghdr_exts.get(ext, ext)
