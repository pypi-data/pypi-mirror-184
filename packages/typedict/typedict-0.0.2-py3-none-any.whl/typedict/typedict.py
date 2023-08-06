from collections import UserDict
from typing import Any, Hashable


class HashableType(Hashable, type):
    ...


class TypeDict(UserDict):
    def __getitem__(self, key: Hashable) -> Any:
        _key = _gettype(key)
        return self.data[_key]

    def __setitem__(self, key: Hashable, value: Any) -> None:
        _key = _gettype(key)
        self.data[_key] = value


def _gettype(value) -> type:
    if type(value) is type:
        return value
    else:
        return type(value)