#!/usr/bin/env python3
"""A module that implements an to_kv() function
"""
import math
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of a string and an int or float"""
    return k, math.pow(v, 2)
