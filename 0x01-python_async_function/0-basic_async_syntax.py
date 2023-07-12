#!/usr/bin/env python3
"""
asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    returns a random wait time between 0 and max_delay
    """
    return random.uniform(0, max_delay)
