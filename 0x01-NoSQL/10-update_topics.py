#!/usr/bin/env python3
"""This module contains a function that update a document in a collection
"""


def update_topics(mongo_collection, name, topics):
    """update a document into a collection"""
    if isinstance(name, str) and all([isinstance(item, str) for item in topics]):
        mongo_collection.update({"name": name}, {"$set": {"topics": topics}})
