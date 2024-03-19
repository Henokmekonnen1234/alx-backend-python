#!/usr/bin/env python3
"""
module 3-tasks.py
"""

import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """In this function it will create task and return it

    Attribs:
        max_delay (int): integer value maximum dealy

    Returns:
        asyncio.Task: return task using wait_random function
    """
    return asyncio.create_task(wait_random(max_delay))
