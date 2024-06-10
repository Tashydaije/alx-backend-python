#!/usr/bin/env python3

"""Module containing a coroutine that waits for a random delay
    then returns the delay count
"""
import asyncio
from typing import List, Awaitable

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns coroutines n times

        Calls the wait_random function n times and returns a list
        of all the delay times

        Parameters
        ----------
        n (int): Number of times to spawn a coroutine
        max_delay (int): The maximum delay the coroutine can wait

        Returns
        -------
        List: A list of all the random delays that were chosen
        in ascending order
    """
    tasks: List[Awaitable] = []
    delay_list: List[float] = []
    for _ in range(0, n, 1):
        # Schedule the task
        task = asyncio.create_task(wait_random(max_delay))
        # Each task updates the delay list with their delay time
        task.add_done_callback(lambda delay: delay_list.append(delay.result()))
        tasks.append(task)
    # Wait for tasks to run concurrently then get the delays
    await asyncio.gather(*tasks)
    return delay_list
