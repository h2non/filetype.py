#!/usr/bin/env python

import os
import sys
import atheris

import filetype


def fuzz(data):
    try:
        filetype.guess(data)
    except (TypeError):
        # catch documented exception
        pass


if __name__ == "__main__":
    atheris.instrument_all()
    # max_len is limit of produced data
    atheris.Setup(sys.argv + ["-max_len=262"], fuzz, internal_libfuzzer=True, enable_python_coverage=True)
    atheris.Fuzz()
