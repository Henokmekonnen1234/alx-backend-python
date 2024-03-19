#!/usr/bin/env python3
"""
Module 1-async_comprehension.py
"""

import asyncio
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """this will return list of random 10 numbers
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return result
