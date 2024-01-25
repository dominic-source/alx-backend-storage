#!/usr/bin/env python3

"""This module implement a cache storage for web"""
import redis
import requests
from functools import wraps
from typing import Callable
import time


def track_url(func: Callable) -> Callable:
    """Track url of a web app"""

    def track(*args, **kwargs):
        """Track url now"""
        r = redis.Redis(db=5)
        key = f"count:{args[0]}"
        r.incr(key)
        r.expire(key, 10)
        result = func(*args, **kwargs)
        return result
    return track


@track_url
def get_page(url: str) -> str:
    """get a page from a website"""
    resp = requests.get(url)
    return resp.text


if __name__ == '__main__':

    r = redis.Redis(db=5)
    get_page('https://google.com')
    get_page('https://google.com')
    get_page('https://google.com')
    print(r.get("count:https://google.com"))
    time.sleep(11)
    get_page('https://google.com')
    print(r.get("count:https://google.com"))
