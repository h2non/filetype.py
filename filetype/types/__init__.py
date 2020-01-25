# -*- coding: utf-8 -*-

from __future__ import absolute_import

from . import application
from . import archive
from . import audio
from . import document
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
    image.Dwg(),
)

# Supported video types
VIDEO = (
    video.M4v(),
    video.Mkv(),
    video.Webm(),
    video.Mov(),
    video.Avi(),
    video.Wmv(),
    video.Mpeg(),
    video.Flv(),
    video.Mp4(),
    video.Match3gp(),
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
    audio.Aac(),
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
    archive.Rpm(),
    archive.Elf(),
    archive.Dcm(),
    archive.Iso(),
)

# Supported application types
APPLICATION = (
    application.Wasm(),
)

# Supported application types
DOCUMENT = (
    document.Doc(),
    document.Xls(),
    document.Ppt(),
)


# Expose supported type matchers
TYPES = list(VIDEO + IMAGE + AUDIO + FONT + ARCHIVE + APPLICATION + DOCUMENT)
