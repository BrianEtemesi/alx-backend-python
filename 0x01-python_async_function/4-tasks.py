#!/usr/bin/env python3
"""
defines an async function to spawn an imported function
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns `task_wait_random` n times
    """
    array = [task_wait_random(max_delay) for _ in range(n)]
    sorted_array = []
    for i in asyncio.as_completed(array):
        r = await i
        sorted_array.append(r)
    return sorted_array

if __name__ == '__main__':
    print(asyncio.run(task_wait_n(5, 10)))
