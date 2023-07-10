#!/usr/bin/env python3
"""This module holds the implementation for `task_wait_random`
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """creates a Task object for a coroutine"""
    return asyncio.create_task(wait_random(max_delay))
