#!/usr/bin/env python3
"""This module contains a function that update a document in a collection
"""
from pymongo import MongoClient


def display_stats():
    """update a document into a collection"""
    client = MongoClient()
    collection = client.logs.nginx

    # Defining the conditions
    conditions = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    values = []
    # Create pipeline and their match condition
    for condition in conditions:
        pipeline = [
            {
                "$match": {"method": condition},
                },
            {
                "$count": f"occurrences"
            }]
        result = list(collection.aggregate(pipeline))
        data = result[0][f"occurrences"] if result else 0
        values.append(data)

    stat = collection.find({"path": "/status"}).count()
    print(f'{collection.count()} logs')
    print("Methods:")
    for idx, cond in enumerate(conditions):
        print(f'\tmethod {cond}: {values[idx]}')

    print(f"{stat} status check")


if __name__ == '__main__':
    display_stats()
