filetype.py |Build Status| |PyPI| |Pyversions| |API|
====================================================

Small and dependency free `Python`_ package to infer file type and MIME
type checking the `magic numbers`_ signature of a file or buffer.

This is a Python port from `filetype`_ Go package.

Features
--------

-  Simple and friendly API
-  Supports a `wide range`_ of file types
-  Provides file extension and MIME type inference
-  File discovery by extension or MIME type
-  File discovery by kind (image, video, audio…)
-  `Pluggable`_: add new custom type matchers
-  `Fast`_, even processing large files
-  Only first 261 bytes representing the max file header is required, so
   you can just `pass a list of bytes`_
-  Dependency free (just Python code, no C extensions, no libmagic
   bindings)
-  Cross-platform file recognition

Installation
------------

::

    pip install filetype

API
---

See `annotated API reference`_.

Examples
--------

Simple file type checking
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    import filetype

    def main():
        kind = filetype.guess('tests/fixtures/sample.jpg')
        if kind is None:
            print('Cannot guess file type!')
            return

        print('File extension: %s' % kind.extension)
        print('File MIME type: %s' % kind.mime)

    if __name__ == '__main__':
        main()

Supported types
---------------

Image
^^^^^

-  **jpg** - ``image/jpeg``
-  **jpx** - ``image/jpx``
-  **png** - ``image/png``
-  **gif** - ``image/gif``
-  **webp** - ``image/webp``
-  **cr2** - ``image/x-canon-cr2``
-  **tif** - ``image/tiff``
-  **bmp** - ``image/bmp``
-  **jxr** - ``image/vnd.ms-photo``
-  **psd** - ``image/vnd.adobe.photoshop``
-  **ico** - ``image/x-icon``
-  **heic** - ``image/heic``
-  **dwg** - ``image/vnd.dwg``

Video
^^^^^

-  **mp4** - ``video/mp4``
-  **m4v** - ``video/x-m4v``
-  **mkv** - ``video/x-matroska``
-  **webm** - ``video/webm``
-  **mov** - ``video/quicktime``
-  **avi** - ``video/x-msvideo``
-  **wmv** - ``video/x-ms-wmv``
-  **mpg** - ``video/mpeg``
-  **flv** - ``video/x-flv``
-  **3gp** - ``video/3gpp``

Audio
^^^^^

-  **mid** - ``audio/midi``
-  **mp3** - ``audio/mpeg``
-  **m4a** - ``audio/m4a``
-  **ogg** - ``audio/ogg``
-  **flac** - ``audio/x-flac``
-  **wav** - ``audio/x-wav``
-  **amr** - ``audio/amr``
-  **aac** - ``audio/aac``

Application
^^^^^^^^^^^

-  **wasm** - ``application/wasm``


Archive
^^^^^^^

-  **epub** - ``application/epub+zip``
-  **zip** - ``application/zip``
-  **tar** - ``application/x-tar``
-  **rar** - ``application/x-rar-compressed``
-  **gz** - ``application/gzip``
-  **bz2** - ``application/x-bzip2``
-  **7z** - ``application/x-7z-compressed``
-  **xz** - ``application/x-xz``
-  **pdf** - ``application/pdf``
-  **exe** - ``application/x-msdownload``
-  **swf** - ``application/x-shockwave-flash``

-  **rtf** - ``application/rtf``
-  **eot** - ``application/octet-stream``
-  **ps** - ``application/postscript``
-  **sqlite** - ``application/x-sqlite3``
-  **nes** - ``application/x-nintendo-nes-rom``
-  **crx** - ``application/x-google-chrome-extension``
-  **cab** - ``application/vnd.ms-cab-compressed``
-  **deb** - ``application/x-deb``
-  **ar** - ``application/x-unix-archive``
-  **Z** - ``application/x-compress``
-  **lz** - ``application/x-lzip``

-  **rpm** - ``application/x-rpm``
-  **elf** - ``application/x-executable``
-  **dcm** - ``application/dicom``
-  **iso** - ``application/x-iso9660-image``

Font
^^^^

-  **woff** - ``application/font-woff``
-  **woff2** - ``application/font-woff``
-  **ttf** - ``application/font-sfnt``
-  **otf** - ``application/font-sfnt``

Document
^^^^^^^^
-  **doc** - ``application/msword``
-  **xls** - ``application/vnd.ms-excel``
-  **ppt** - ``application/vnd.ms-powerpoint``


.. _Python: http://python.org
.. _magic numbers: https://en.wikipedia.org/wiki/Magic_number_(programming)#Magic_numbers_in_files
.. _filetype: https://github.com/h2non/filetype
.. _wide range: #supported-types
.. _Pluggable: #add-additional-file-type-matchers
.. _Fast: #benchmarks
.. _pass a list of bytes: #file-header
.. _annotated API reference: https://h2non.github.io/filetype.py/

.. |Build Status| image:: https://travis-ci.org/h2non/filetype.py.svg?branch=master
   :target: https://travis-ci.org/h2non/filetype.py
.. |PyPI| image:: https://img.shields.io/pypi/v/filetype.svg?maxAge=2592000?style=flat-square
   :target: https://pypi.python.org/pypi/filetype
.. |Pyversions| image:: https://img.shields.io/pypi/pyversions/filetype.svg?style=flat-square
    :target: https://pypi.python.org/pypi/filetype
.. |API| image:: https://img.shields.io/badge/api-docs-green.svg
   :target: https://h2non.github.io/filetype.py
