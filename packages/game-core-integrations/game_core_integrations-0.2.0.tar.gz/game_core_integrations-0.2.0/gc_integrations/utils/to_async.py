import asyncio
from functools import wraps, partial
from typing import Any


def to_async(func: Any):
    """
    Decorator to convert a function to an async function.
    :param func: the function to convert
    :return:
    """

    @wraps(func)
    async def run_async(*args, **kwargs):
        loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        await loop.run_in_executor(None, pfunc)
