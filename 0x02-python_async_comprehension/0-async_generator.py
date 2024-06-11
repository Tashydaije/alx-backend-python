#!/usr/bin/env python3

""" A coroutine called async_generator that takes no arguments"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times and yields a random number in [0..10]

        In each loop, the generator waits for 1 second then
        yields a random number between 0 and 10

        Parameters
        ----------
        None

        Yields
        ------
        Random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
