#!/usr/bin/env python3
"""This module holds the implementation to the measure_runtime function
"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measures the runtime for concurrently running 4 async comprehensions"""
    tasks = []
    for _ in range(4):
        task = asyncio.create_task(async_comprehension())
        tasks.append(task)
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
