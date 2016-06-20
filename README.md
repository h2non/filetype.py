# filetype.py [![Build Status](https://travis-ci.org/h2non/filetype.py.svg?branch=master)](https://travis-ci.org/h2non/filetype.py) [![PyPI](https://img.shields.io/pypi/dm/filetype.svg?maxAge=2592000?style=flat-square)](https://pypi.python.org/pypi/filetype) [![PyPI](https://img.shields.io/pypi/v/filetype.svg?maxAge=2592000?style=flat-square)](https://pypi.python.org/pypi/filetype) [![API](https://img.shields.io/badge/api-docs-green.svg)](https://h2non.github.io/filetype.py)

Small and dependency free [Python](http://python.org) package to infer file type and MIME type checking the [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) signature of a file or buffer.

This is a Python port from [filetype](https://github.com/h2non/) Go package. 
Works in Python `+3`.

## Features

- Simple and friendly API
- Supports a [wide range](#supported-types) of file types
- Provides file extension and MIME type inference
- File discovery by extension or MIME type 
- File discovery by kind (image, video, audio...)
- [Pluggable](#add-additional-file-type-matchers): add new custom type matchers 
- [Fast](#benchmarks), even processing large files
- Only first 261 bytes representing the max file header is required, so you can just [pass a list of bytes](#file-header)
- Dependency free (just Python code, no C extensions, no libmagic bindings)
- Cross-platform file recognition

## Installation

```bash
pip install filetype
```

## API

See [annotated API reference](https://h2non.github.io/filetype.py/).

## Examples

#### Simple file type checking

```python
import filetype

def main():
  kind = filetype.guess_type('tests/fixtures/sample.jpg')
  if kind is None:
    print('Cannot guess file type!')
    return

  print('File extension: %s' % kind.extension)
  print('File MIME type: %s' % kind.mime)

if __name__ == '__main__':
  main()
```

## Supported types

#### Image

- **jpg** - `image/jpeg`
- **png** - `image/png`
- **gif** - `image/gif`
- **webp** - `image/webp`
- **cr2** - `image/x-canon-cr2`
- **tif** - `image/tiff`
- **bmp** - `image/bmp`
- **jxr** - `image/vnd.ms-photo`
- **psd** - `image/vnd.adobe.photoshop`
- **ico** - `image/x-icon`

#### Video

- **mp4** - `video/mp4`
- **m4v** - `video/x-m4v`
- **mkv** - `video/x-matroska`
- **webm** - `video/webm`
- **mov** - `video/quicktime`
- **avi** - `video/x-msvideo`
- **wmv** - `video/x-ms-wmv`
- **mpg** - `video/mpeg`
- **flv** - `video/x-flv`

#### Audio

- **mid** - `audio/midi`
- **mp3** - `audio/mpeg`
- **m4a** - `audio/m4a`
- **ogg** - `audio/ogg`
- **flac** - `audio/x-flac`
- **wav** - `audio/x-wav`
- **amr** - `audio/amr`

#### Archive

- **epub** - `application/epub+zip`
- **zip** - `application/zip`
- **tar** - `application/x-tar`
- **rar** - `application/x-rar-compressed`
- **gz** - `application/gzip`
- **bz2** - `application/x-bzip2`
- **7z** - `application/x-7z-compressed`
- **xz** - `application/x-xz`
- **pdf** - `application/pdf`
- **exe** - `application/x-msdownload`
- **swf** - `application/x-shockwave-flash`
- **rtf** - `application/rtf`
- **eot** - `application/octet-stream`
- **ps** - `application/postscript`
- **sqlite** - `application/x-sqlite3`
- **nes** - `application/x-nintendo-nes-rom`
- **crx** - `application/x-google-chrome-extension`
- **cab** - `application/vnd.ms-cab-compressed`
- **deb** - `application/x-deb`
- **ar** - `application/x-unix-archive`
- **Z** - `application/x-compress`
- **lz** - `application/x-lzip`

#### Font

- **woff** - `application/font-woff`
- **woff2** - `application/font-woff`
- **ttf** - `application/font-sfnt`
- **otf** - `application/font-sfnt`

## Benchmarks

Measured using [real files](https://github.com/h2non/filetype.py/tree/master/tests/fixtures). 

Environment: OSX x64 i7 2.7 Ghz

```bash
------------------------------------------------------------------------------------------ benchmark: 7 tests ------------------------------------------------------------------------------------------
Name (time in ns)                       Min                     Max                   Mean                StdDev                 Median                   IQR            Outliers(*)  Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_infer_image_from_bytes        357.6279 (1.0)       29,166.5395 (1.0)       1,642.3360 (1.0)        380.9934 (1.0)       1,509.9843 (1.0)        158.9457 (1.0)       9095;13752  102301           6
test_infer_audio_from_bytes        953.6743 (2.67)      96,082.6874 (3.29)     16,534.5880 (10.07)    3,002.1143 (7.88)     15,974.0448 (10.58)      953.6743 (6.00)       4514;6051   41528           1
test_infer_video_from_bytes     13,828.2776 (38.67)    272,989.2731 (9.36)     16,151.3144 (9.83)     3,361.2320 (8.82)     15,020.3705 (9.95)       953.6743 (6.00)       2522;2887   22193           1
test_infer_image_from_disk      15,974.0448 (44.67)    108,957.2906 (3.74)     18,621.0844 (11.34)    3,895.4441 (10.22)    17,166.1377 (11.37)    1,192.0929 (7.50)       1528;1804   10206           1
test_infer_video_from_disk      23,841.8579 (66.67)    229,120.2545 (7.86)     28,691.3476 (17.47)    6,242.9901 (16.39)    25,987.6251 (17.21)    4,053.1158 (25.50)      1987;1247   15651           1
test_infer_zip_from_disk        26,941.2994 (75.33)    230,073.9288 (7.89)     32,123.3861 (19.56)    7,524.4988 (19.75)    29,087.0667 (19.26)    4,768.3716 (30.00)      1349;1292   16132           1
test_infer_tar_from_disk        33,855.4382 (94.67)    164,031.9824 (5.62)     36,884.4401 (22.46)    4,489.4443 (11.78)    36,001.2054 (23.84)      953.6743 (6.00)       1036;1828   14666           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

## License

MIT - Tomas Aparicio