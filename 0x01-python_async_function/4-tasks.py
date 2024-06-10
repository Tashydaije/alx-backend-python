#!/usr/bin/env python3

"""Module containing a coroutine that waits for a random delay
    for several tasks to execute then returns the delays
"""
import asyncio
from typing import List, Awaitable

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns coroutines n times and waits for them

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
        # Create task
        task: asyncio.Task = task_wait_random(max_delay)
        # Each task updates the delay list with their delay time
        task.add_done_callback(lambda delay: delay_list.append(delay.result()))
        tasks.append(task)
    # Wait for tasks to run concurrently then get the delays
    await asyncio.gather(*tasks)
    return delay_list  # Already in ascending order due to concurrency
