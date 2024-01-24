#!/usr/bin/env python3
"""This module contains a function that update a document in a collection
"""

from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """update a document into a collection"""
    if isinstance(name, str) and all([isinstance(item, str) for item in topics]):
        mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
