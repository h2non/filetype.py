# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os

import filetype

# Absolute path to fixtures directory
FIXTURES = os.path.dirname(os.path.abspath(__file__)) + '/fixtures'


def test_infer_image_from_disk(benchmark):
    benchmark(filetype.guess, FIXTURES + '/sample.jpg')


def test_infer_video_from_disk(benchmark):
    benchmark(filetype.guess, FIXTURES + '/sample.mp4')


def test_infer_zip_from_disk(benchmark):
    benchmark(filetype.guess, FIXTURES + '/sample.zip')


def test_infer_tar_from_disk(benchmark):
    benchmark(filetype.guess, FIXTURES + '/sample.tar')


def test_infer_image_from_bytes(benchmark):
    benchmark(filetype.guess,
              bytearray([0xFF, 0xD8, 0xFF, 0x00, 0x08]))


def test_infer_video_from_bytes(benchmark):
    benchmark(filetype.guess,
              bytearray([0x1A, 0x45, 0xDF, 0xA3, 0x08]))


def test_infer_audio_from_bytes(benchmark):
    benchmark(filetype.guess,
              bytearray([0x4D, 0x54, 0x68, 0xA3, 0x64]))
