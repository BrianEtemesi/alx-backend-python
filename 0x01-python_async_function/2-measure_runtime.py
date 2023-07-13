#!/usr/bin/env python3
"""
defines a function to measures total execution
time of an async function
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures total execution time of an async function
    """
    start_time = time.monotonic()
    asyncio.run(wait_n(n, max_delay))
    return (time.monotonic() - start_time) / n

if __name__ == '__main__':
    print(measure_time(5, 9))
