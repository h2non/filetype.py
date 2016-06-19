# filetype.py

Small and dependency free [Python](http://python.org) package to infer file type and MIME type checking the [magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files) signature of a file or buffer.

This is a Python port from [filetype](https://github.com/h2non/) Go package.

## Features

- Supports a [wide range](#supported-types) of file types
- Provides file extension and proper MIME type
- File discovery by extension or MIME type 
- File discovery by class (image, video, audio...)
- Provides a bunch of helpers and file matching shortcuts
- [Pluggable](#add-additional-file-type-matchers): add custom new types and matchers 
- Simple and semantic API
- [Blazing fast](#benchmarks), even processing large files
- Only first 261 bytes representing the max file header is required, so you can just [pass a slice](#file-header)
- Dependency free (just Go code, no C compilation needed)
- Cross-platform file recognition

## Installation

```bash
pip install filetype
```

## API

See [read the docs](https://godoc.org/github.com/h2non/filetype) API reference.

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

Measured using [real files](https://github.com/h2non/filetype/tree/master/fixturess). 

Environment: OSX x64 i7 2.7 Ghz

```bash
BenchmarkMatchTar-8    1000000        1083 ns/op
BenchmarkMatchZip-8    1000000        1162 ns/op
BenchmarkMatchJpeg-8   1000000        1280 ns/op
BenchmarkMatchGif-8    1000000        1315 ns/op
BenchmarkMatchPng-8    1000000        1121 ns/op
```

## License

MIT - Tomas Aparicio