#!/usr/bin/env python3
"""
defines an async function to spawn an imported function
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns `wait_random` n times
    """
    array = [wait_random(max_delay) for _ in range(n)]
    sorted_array = []
    for i in asyncio.as_completed(array):
        r = await i
        sorted_array.append(r)
    return sorted_array

if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 10)))
