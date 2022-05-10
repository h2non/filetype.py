# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

import filetype

import pytest

from . import FIXTURES


@pytest.mark.parametrize("mime,ext,filename",
                         [
                             ('image/jpeg', 'jpg', 'sample.jpg'),
                             ('image/png', 'png', 'sample.png'),
                             ('image/jpx', 'jpx', 'sample.jpx'),
                             ('image/gif', 'gif', 'sample.gif'),
                             ('image/heic', 'heic', 'sample.heic'),
                             ('image/tiff', 'tif', 'sample.tif'),
                             ('video/mp4', 'mp4', 'sample.mp4'),
                             ('video/quicktime', 'mov', 'sample.mov'),
                         ])
def test_guess_filetype(mime, ext, filename):
    kind = filetype.guess(os.path.join(FIXTURES, filename))

    assert kind is not None
    assert kind.mime == mime
    assert kind.extension == ext
