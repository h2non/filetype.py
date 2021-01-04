# -*- coding: utf-8 -*-

# Python 2.7 workaround
try:
    import pathlib
except ImportError:
    pass


_NUM_SIGNATURE_BYTES = 262


def get_signature_bytes(path):
    """
    Reads file from disk and returns the first 262 bytes
    of data representing the magic number header signature.

    Args:
        path: path string to file.

    Returns:
        First 262 bytes of the file content as bytearray type.
    """
    with open(path, 'rb') as fp:
        return bytearray(fp.read(_NUM_SIGNATURE_BYTES))


def signature(array):
    """
    Returns the first 262 bytes of the given bytearray
    as part of the file header signature.

    Args:
        array: bytearray to extract the header signature.

    Returns:
        First 262 bytes of the file content as bytearray type.
    """
    length = len(array)
    index = _NUM_SIGNATURE_BYTES if length > _NUM_SIGNATURE_BYTES else length

    return array[:index]


def get_bytes(obj):
    """
    Infers the input type and reads the first 262 bytes,
    returning a sliced bytearray.

    Args:
        obj: path to readable, file, bytes or bytearray.

    Returns:
        First 262 bytes of the file content as bytearray type.

    Raises:
        TypeError: if obj is not a supported type.
    """
    try:
        obj = obj.read(_NUM_SIGNATURE_BYTES)
    except AttributeError:
        # duck-typing as readable failed - we'll try the other options
        pass

    kind = type(obj)

    if kind is bytearray:
        return signature(obj)

    if kind is str:
        return get_signature_bytes(obj)

    if kind is bytes:
        return signature(obj)

    if kind is memoryview:
        return signature(obj).tolist()

    if isinstance(obj, pathlib.PurePath):
        return get_signature_bytes(obj)

    raise TypeError('Unsupported type as file input: %s' % kind)
