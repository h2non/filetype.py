# -*- coding: utf-8 -*-


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
        return bytearray(fp.read(262))


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
    index = 262 if length > 262 else length

    return array[:index]


def get_bytes(obj):
    """
    Infers the input type and reads the first 262 bytes,
    returning a sliced bytearray.

    Args:
        obj: path to file, bytes or bytearray.

    Returns:
        First 262 bytes of the file content as bytearray type.

    Raises:
        TypeError: if obj is not a supported type.
    """
    kind = type(obj)

    if kind is bytearray:
        return signature(obj)

    if kind is str:
        return get_signature_bytes(obj)

    if kind is bytes:
        return signature(obj)

    if kind is memoryview:
        return signature(obj).tolist()

    raise TypeError('Unsupported type as file input: %s' % kind)
