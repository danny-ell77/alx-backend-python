#!/usr/bin/env python3
"""This module holds the implementation for `wait_n`
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """executes multiple sleep coroutines concurrently"""
    tasks = []
    i = 0
    while i < n:
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
        i += 1
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
