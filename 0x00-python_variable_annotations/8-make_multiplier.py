#!/usr/bin/env python3
"""A module that implements an make_multiplier() function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier"""
    return lambda value: value * multiplier
