from collections import UserDict
from typing import Any, Hashable


class HashableType(Hashable, type):
    ...


class TypeDict(UserDict):
    ...