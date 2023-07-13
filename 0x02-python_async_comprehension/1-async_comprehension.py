#!/usr/bin/env python3
"""
async function
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    returns numbers from a generator
    """
    return [i async for i in async_generator()]


if __name__ == '__main__':
    print(asyncio.run(async_comprehension()))
