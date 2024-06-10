#!/usr/bin/env python3

"""Module containing a method that returns an asyncio.Task
"""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns an asyncio task

        Parameters
        ----------
        max_delay (float): The maximum delay the coroutine can wait

        Returns
        -------
        asyncio.Task: An asynchronous task
    """
    return asyncio.create_task(wait_random(max_delay))
