#!/usr/bin/env python3

"""Write some strings to redis module
"""
import redis
import uuid


class Cache:
    """The cache class for the application"""

    def __init__(self):
        """Init method for the class"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: any) -> str:
        """Take a data argument and return a string"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
