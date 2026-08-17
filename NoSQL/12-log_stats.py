#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")
    db = client.logs
    collection = db.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    print("{} status check".format(status_count))
