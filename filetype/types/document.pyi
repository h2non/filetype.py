import __future__ as _future
import typing as _typing

from .base import Type as Type, _Buffer as _Buffer

absolute_import: _future._Feature

class ZippedDocumentBase(Type):
    def match(self, buf: _Buffer) -> _typing.Optional[bool]: ...
    def match_document(self, buf: _Buffer) -> _typing.Optional[bool]: ...
    def compare_bytes(
        self, buf: _Buffer, subslice: bytes, start_offset: int
    ) -> bool: ...
    def search_signature(
        self, buf: _Buffer, start: int, rangeNum: int
    ) -> int: ...

class OpenDocument(ZippedDocumentBase):
    def match_document(self, buf: _Buffer) -> _typing.Optional[bool]: ...

class OfficeOpenXml(ZippedDocumentBase):
    def match_document(self, buf: _Buffer) -> _typing.Optional[bool]: ...
    def match_filename(
        self, buf: _Buffer, offset: int
    ) -> _typing.Optional[bool]: ...

class Doc(Type):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
    def match(self, buf: _Buffer) -> bool: ...

class Docx(OfficeOpenXml):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...

class Odt(OpenDocument):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...

class Xls(Type):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
    def match(self, buf: _Buffer) -> bool: ...

class Xlsx(OfficeOpenXml):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...

class Ods(OpenDocument):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...

class Ppt(Type):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
    def match(self, buf: _Buffer) -> bool: ...

class Pptx(OfficeOpenXml):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...

class Odp(OpenDocument):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
