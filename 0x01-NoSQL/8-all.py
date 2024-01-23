#!/usr/bin/env python3

"""This module contains a function that list all document in a collection
"""
from pymongo import MongoClient
import json
from bson import json_util


def list_all(mongo_collection):
    """list all collection of a database"""
    if value := mongo_collection.find():
        return value
    return []
