import __future__ as _future

from .base import Type as Type, _Buffer as _Buffer

absolute_import: _future._Feature

class Woff(Type):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
    def match(self, buf: _Buffer) -> bool: ...

class Woff2(Type):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
    def match(self, buf: _Buffer) -> bool: ...

class Ttf(Type):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
    def match(self, buf: _Buffer) -> bool: ...

class Otf(Type):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
    def match(self, buf: _Buffer) -> bool: ...
