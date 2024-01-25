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
        hash_c = "count_url"
        key = f"count:{args[0]}"
        r.hincrby(hash_c, key, 1)
        r.expire(hash_c, 10)
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
    get_page('http://slowwly.robertomurray.co.uk')
    get_page('https://google.com')
    get_page('https://google.com')
    print(r.hgetall("count_url"))
    time.sleep(15)
    get_page('http://slowwly.robertomurray.co.uk')
    get_page('http://slowwly.robertomurray.co.uk')
    print(r.hgetall("count_url"))
