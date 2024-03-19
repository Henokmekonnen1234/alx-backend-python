#!/usr/bin/env python3
"""
Module 2-measure_runtime.py
"""

import asyncio
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    In this function it will measure the time and return it
    """
    value = [async_comprehension() for _ in range(4)]
    start_time = time.time()
    await asyncio.gather(*value)
    end_time = time.time()
    return end_time - start_time
