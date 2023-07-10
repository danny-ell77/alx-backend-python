#!/usr/bin/env python3
"""This script holds the implementation for `wait_random`
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """generate random sleep delay for coroutine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
