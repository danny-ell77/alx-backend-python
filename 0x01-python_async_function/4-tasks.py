#!/usr/bin/env python3
"""This module holds the implementation for `task_wait_n`
"""
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n, max_delay):
    """executes multiple sleep coroutines concurrently"""
    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)
    delays = await asyncio.gather(*tasks)
    delays.sort()
    return delays
