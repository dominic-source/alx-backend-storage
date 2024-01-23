#!/usr/bin/env python3
"""This module contains a function that insert document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """Insert an document into a collection"""
    
    value = mongo_collection.insert(kwargs)
    return value
