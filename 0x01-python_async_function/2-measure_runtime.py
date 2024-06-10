#!/usr/bin/env python3

"""Module containing a method that measures the runtime of wait_n
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures the time taken to run wait_n n times

        Calls the wait_n function n times and returns the runtime

        Parameters
        ----------
        n (int): Number of times to run wait_n
        max_delay (float): The maximum delay the coroutine can wait

        Returns
        -------
        float: The runtime of execting wait_n
    """
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.perf_counter()

    total_time: float = end_time - start_time

    return total_time / n
