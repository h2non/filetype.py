import __future__ as _future

from .base import Type as Type, _Buffer as _Buffer

absolute_import: _future._Feature

class Wasm(Type):
    MIME: str
    EXTENSION: str
    def __init__(self) -> None: ...
    def match(self, buf: _Buffer) -> bool: ...
