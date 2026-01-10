# -*- coding: utf-8 -*-


class Type:
    """
    Represents the file type object inherited by
    specific file type matchers.
    Provides convenient accessor and helper methods.
    """
    def __init__(self, mime: str, extension: str):
        self.__mime = mime
        self.__extension = extension

    @property
    def mime(self) -> str:
        return self.__mime

    @property
    def extension(self) -> str:
        return self.__extension

    def is_extension(self, extension: str) -> bool:
        return self.__extension is extension

    def is_mime(self, mime: str) -> bool:
        return self.__mime is mime

    def match(self, buf: bytes) -> bool:
        raise NotImplementedError
