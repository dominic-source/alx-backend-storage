#!/usr/bin/env python3

"""Write some strings to redis module
"""
import redis
import uuid
from typing import Union
from functools import wraps


def count_calls(Callable):
    """a decorator function for cache"""

    @wraps(Callable)
    def func(self, *args, **kwargs):
        """decorator for a class"""

        key = Callable.__qualname__
        self._redis.incr(key)
        return Callable(self, *args, **kwargs)
    return func


class Cache:
    """The cache class for the application"""

    def __init__(self) -> None:
        """Init method for the class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Take a data argument and return a string"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
        """"REturn the original value"""

        data = self._redis.get(key)
        if data:
            if fn:
                return fn(data)
            return data
        return data

    def get_str(self, key: str) -> Union[str, int]:
        """return the string of the data"""

        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """return the int data"""

        return self.get(key, int)
