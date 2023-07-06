#!/usr/bin/env python3
"""A module that implements an safely_get_value() function
"""
from typing import Mapping, TypeVar, Any, Union

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """Safely return the value of a key in a Mapping"""
    if key in dct:
        return dct[key]
    else:
        return default
