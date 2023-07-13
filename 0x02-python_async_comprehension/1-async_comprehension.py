#!/usr/bin/env python3
"""This module holds the implementation to the async_comprehension function
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """returns a list of floats from a generator"""
    return [i async for i in async_generator()]
