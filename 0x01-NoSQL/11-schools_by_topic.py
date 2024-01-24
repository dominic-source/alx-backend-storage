#!/usr/bin/env python3
"""This module contains a function that update a document in a collection
"""


def schools_by_topic(mongo_collection, topics):
    """update a document into a collection"""
    return mongo_collection.find({"topics": topics})
