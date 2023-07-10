#!/usr/bin/env python3
"""This script holds the implementation for `wait_random`
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """generate random sleep delay fro coroutine"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
