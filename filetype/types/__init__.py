# -*- coding: utf-8 -*-

from . import font
from . import image
from . import video
from . import audio
from . import archive
from .base import Type  # noqa

# Supported image types
image = (
    image.Jpeg(),
    image.Png(),
    image.Gif(),
    image.Webp(),
    image.Cr2(),
    image.Tiff(),
    image.Bmp(),
    image.Jxr(),
    image.Psd(),
    image.Ico(),
)

# Supported video types
video = (
    video.Mp4(),
    video.M4v(),
    video.Mkv(),
    video.Mov(),
    video.Avi(),
    video.Wmv(),
    video.Mpeg(),
)

# Supported audio types
audio = (
    audio.Midi(),
    audio.Mp3(),
    audio.M4a(),
    audio.Ogg(),
    audio.Flac(),
    audio.Wav(),
    audio.Amr(),
)

# Supported font types
font = (
    font.Woff(),
    font.Woff2(),
    font.Ttf(),
    font.Otf(),
)

# Supported archive container types
archive = (
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
types = list(image + audio +
             font + video + archive)
