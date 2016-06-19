# -*- coding: utf-8 -*-


def get_signature_bytes(path):
    """
    Reads file from disk and returns the first 256 bytes
    of data representing the magic number header signature.

    :param path str
    :rtype bytes
    """
    with open(path, 'rb') as f:
        return f.read(256)
