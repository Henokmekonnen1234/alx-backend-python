#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines.py
In this module we will see about asyncio
"""

import asyncio


async def wait_n(n: int, max_delay: int) -> list[float]:
    """ In this module we will return the list of delay time

    Attribs:
        n (int): int value for repetition
        max_delay (int): max delay time int value

    Returns:
        list[float]: returns the values of list of delays
    """
    wait_r = __import__("0-basic_async_syntax").wait_random
    value = [wait_r(max_delay) for _ in range(n)]
    result = []
    for returned in asyncio.as_completed(value):
        resp = await returned
        result.append(resp)
    return result
