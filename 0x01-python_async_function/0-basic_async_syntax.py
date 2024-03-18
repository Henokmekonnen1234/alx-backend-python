#!/usr/bin/env python3
"""
Module 0-basic_async_syntax.py
In this module we will implement asyncio concepts
"""

import asyncio
import random

async def wait_random(max_delay=10) -> float:
    """this will generate random number between o and max_delay and
        await using the generated number and returned it
    Attribs:
        max_delay (int): maximum value given to random function

    Returns:
        float: it will return float number
    """
    random_num: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
