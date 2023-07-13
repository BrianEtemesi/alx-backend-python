#!/usr/bin/env python3
"""
coroutine to measure execution time
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    executes an async comprehension 4 times and returns
    total executio time
    """
    start_time = time.monotonic()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    return time.monotonic() - start_time
