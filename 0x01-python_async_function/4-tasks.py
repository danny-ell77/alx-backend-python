#!/usr/bin/env python3
"""This module holds the implementation for `task_wait_n`
"""
import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """executes multiple sleep coroutines concurrently"""
    tasks = []
    i = 0
    while i < n:
        task = task_wait_random(max_delay)
        tasks.append(task)
        i += 1
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
