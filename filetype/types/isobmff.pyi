import __future__ as _future
import codecs as codecs
import typing as _typing

from .base import Type as Type, _Buffer as _Buffer

absolute_import: _future._Feature

class IsoBmff(Type):
    def __init__(self, mime: str, extension: str) -> None: ...
    def _is_isobmff(self, buf: _Buffer) -> bool: ...
    def _get_ftyp(
        self, buf: _Buffer
    ) -> _typing.Tuple[str, int, _typing.List[str]]: ...
