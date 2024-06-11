#!/usr/bin/env python3

""" a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather"""
import asyncio
import time
from typing import Awaitable

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> Awaitable[float]:
    """ Measures the runtime of executing 'async_comprehension' 4 times

        Params: None
        Returns: total runtime
    """
    startTime: float = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    endTime: float = time.perf_counter()

    total_time = endTime - startTime

    return total_time
