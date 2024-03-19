#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines.py
In this module we will see about asyncio
"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ In this module we will return the list of delay time

    Attribs:
        n (int): int value for repetition
        max_delay (int): max delay time int value

    Returns:
        list[float]: returns the values of list of delays
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    results = []
    for future in asyncio.as_completed(coroutines):
        result = await future
        results.append(result)

    return results
