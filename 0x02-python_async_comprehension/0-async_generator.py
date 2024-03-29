#!/usr/bin/env python3
"""
Module 0-async_generator.py
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """In this function a series of float will be send
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
