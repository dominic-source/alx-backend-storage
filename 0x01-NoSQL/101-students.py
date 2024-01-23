#!/usr/bin/env python3
"""This module contains a function that find and
sort a document in a collection
"""
import pymongo


def top_students(mongo_collection):
    """Find students in sorted order"""

    data = mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {
            "$group": {
                "init_id": {"$first": "$_id"},
                "_id": "$name",
                "averageScore": {"$avg": "$topics.score"},
            }
        },
        {
            "$project": {
                "_id": "$init_id",
                "name": "$_id",
                "averageScore": 1
            }
        },
        {
            "$sort": {
                "averageScore": pymongo.DESCENDING
            }
        }
    ])

    return list(data)
