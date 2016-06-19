# -*- coding: utf-8 -*-

from filetype.types import image
from filetype.types import video
from filetype.types import audio
from filetype.types import font
from filetype.types import archive

# Supported image types
image_types = (
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
video_types = (
    video.Mp4(),
    video.M4v(),
    video.Mkv(),
    video.Mov(),
    video.Avi(),
    video.Wmv(),
    video.Mpeg(),
)

# Supported audio types
audio_types = (
    audio.Midi(),
    audio.Mp3(),
    audio.M4a(),
    audio.Ogg(),
    audio.Flac(),
    audio.Wav(),
    audio.Amr(),
)

# Supported archive container types
archive_types = (
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

# Supported archive container types
font_types = (
    font.Woff(),
    font.Woff2(),
    font.Ttf(),
    font.Otf(),
)

# Expose supported type matchers
types = list(image_types + audio_types +
        font_types + video_types +
        archive_types)
