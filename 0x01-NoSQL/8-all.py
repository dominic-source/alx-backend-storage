#!/usr/bin/env python3
"""This module contains a function that list all document in a collection
"""
from typing import List
from pymongo import MongoClient


def list_all(mongo_collection) -> List:
    """list all collection of a database"""

    if value := mongo_collection.find():
        return value
    return []


if __name__ == '__main__':
    client = MongoClient()
    mongo_collection = client.my_db.school
    list_all(mongo_collection)
