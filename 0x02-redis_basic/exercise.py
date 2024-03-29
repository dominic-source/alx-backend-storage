#!/usr/bin/env python3

"""Write some strings to redis module
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """a decorator function for cache"""

    @wraps(method)
    def func(self, *args, **kwargs):
        """decorator for a class"""

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return func


def call_history(method: Callable) -> Callable:
    """count call history"""

    @wraps(method)
    def func(self, *args, **kwargs):
        """track the call history"""

        key_inputs = method.__qualname__ + ":inputs"
        key_outputs = method.__qualname__ + ":outputs"
        self._redis.rpush(key_inputs, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(key_outputs, output)
        return output
    return func


def replay(name):
    """Replay previous call history"""

    r = redis.Redis()
    key_inputs = name.__qualname__ + ":inputs"
    key_outputs = name.__qualname__ + ":outputs"

    inp = r.lrange(key_inputs, 0, -1)
    out = r.lrange(key_outputs, 0, -1)
    print(f'Cache.store was called {len(inp)} times:')
    for i in zip(inp, out):
        print(f'Cache.store(*{i[0].decode("utf-8")}) ' +
              f'-> {i[1].decode("utf-8")}')


class Cache:
    """The cache class for the application"""

    def __init__(self) -> None:
        """Init method for the class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Take a data argument and return a string"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
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
