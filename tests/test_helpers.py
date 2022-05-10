# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

from filetype import helpers

from . import FIXTURES


def test_supported_extension():
    assert helpers.is_extension_supported('jpg') is True


def test_unsupported_extension():
    assert helpers.is_extension_supported('foo') is False


def test_supported_mime():
    assert helpers.is_mime_supported('image/jpeg') is True


def test_unsupported_mime():
    assert helpers.is_mime_supported('foo') is False


def test_is_archive():
    assert helpers.is_archive(os.path.join(FIXTURES, 'sample.tar')) is True


def test_is_font():
    assert helpers.is_font(os.path.join(FIXTURES, 'sample.ttf')) is True


def test_is_image():
    assert helpers.is_image(os.path.join(FIXTURES, 'sample.png')) is True


def test_is_video():
    assert helpers.is_video(os.path.join(FIXTURES, 'sample.mp4')) is True


def test_is_audio():
    assert helpers.is_audio(os.path.join(FIXTURES, 'sample.mp3')) is True
