#!/usr/bin/env python3
"""
defines a coroutine that yields a random number
"""
import random
import asyncio
from typing import AsyncIterator

async def async_generator() -> AsyncIterator[float]:
    """
    asynchronously yield a random number for each loop
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
