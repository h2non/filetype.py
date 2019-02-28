# -*- coding: utf-8 -*-

from __future__ import absolute_import

from . import archive
from . import audio
from . import font
from . import image
from . import video
from .base import Type  # noqa

# Supported image types
IMAGE = (
    image.Jpeg(),
    image.Jpx(),
    image.Png(),
    image.Gif(),
    image.Webp(),
    image.Cr2(),
    image.Tiff(),
    image.Bmp(),
    image.Jxr(),
    image.Psd(),
    image.Ico(),
    image.Heic(),
    image.Dcm(),
)

# Supported video types
VIDEO = (
    video.Mp4(),
    video.M4v(),
    video.Mkv(),
    video.Mov(),
    video.Avi(),
    video.Wmv(),
    video.Mpeg(),
    video.Webm(),
    video.Flv(),
)

# Supported audio types
AUDIO = (
    audio.Midi(),
    audio.Mp3(),
    audio.M4a(),
    audio.Ogg(),
    audio.Flac(),
    audio.Wav(),
    audio.Amr(),
)

# Supported font types
FONT = (font.Woff(), font.Woff2(), font.Ttf(), font.Otf())

# Supported archive container types
ARCHIVE = (
    archive.Epub(),
    archive.Zip(),
    archive.Tar(),
    archive.Rar(),
    archive.Gz(),
    archive.Bz2(),
    archive.SevenZ(),
    archive.Pdf(),
    archive.Exe(),
    archive.Swf(),
    archive.Rtf(),
    archive.Nes(),
    archive.Crx(),
    archive.Cab(),
    archive.Eot(),
    archive.Ps(),
    archive.Xz(),
    archive.Sqlite(),
    archive.Deb(),
    archive.Ar(),
    archive.Z(),
    archive.Lz(),
)

# Expose supported type matchers
TYPES = list(VIDEO + IMAGE + AUDIO + FONT + ARCHIVE)
