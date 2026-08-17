#!/usr/bin/env python3
"""Display statistics about Nginx access logs stored in MongoDB."""

from pymongo import MongoClient


def print_log_stats():
    """Print total, per-method, and status-check Nginx log counts."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")

    for method in ("GET", "POST", "PUT", "PATCH", "DELETE"):
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_checks = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("\t{} status check".format(status_checks))
    client.close()


if __name__ == "__main__":
    print_log_stats()
