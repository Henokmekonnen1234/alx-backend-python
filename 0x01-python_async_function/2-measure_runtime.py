#!/usr/bin/env python3
"""
Module 2-measure_runtime.py
In this module we will see asuncio module
"""

import asyncio


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """In this function we will sum the list of float from wait_n
        function and sum it up and divided by the n

    Attrib:
        n (int): integer value
        max_delay (int): integer value

    Returns:
        float: floating value
    """
    sum = 0
    for i in asyncio.run(wait_n(n, max_delay)):
        sum += i
    return sum / n
