#!/usr/bin/env python3
"""This module holds the implementation to the async_generator function
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async generator that yields random number every 1s"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
