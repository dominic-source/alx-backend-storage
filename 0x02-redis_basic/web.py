#!/usr/bin/env python3

"""This module implement a cache storage for web"""
import redis
import requests
from functools import wraps
from typing import Callable
import time


def track_url(func: Callable) -> Callable:
    """Track url of a web app"""

    def track(*args, **kwargs) -> str:
        """Track url now"""
        r = redis.Redis(db=5)
        key = f"count:{args}"
        r.incrby(key, 1)
        r.expire(key, 10)
        result = func(*args, **kwargs)
        return result
    return track


@track_url
def get_page(url: str) -> str:
    """get a page from a website"""
    resp = requests.get(url)
    return resp.text
