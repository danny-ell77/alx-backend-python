#!/usr/bin/env python3
"""This module holds the implementation for `wait_n`
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """executes multiple sleep coroutines concurrently"""
    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
