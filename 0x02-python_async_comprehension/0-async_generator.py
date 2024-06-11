#!/usr/bin/env python3

""" A coroutine called async_generator that takes no arguments"""

import asyncio
import random


async def async_generator():
    """ coroutine func that yields a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
