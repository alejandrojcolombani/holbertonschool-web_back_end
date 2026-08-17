#!/usr/bin/env python3
"""Provide a helper for listing all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return a list containing every document from ``mongo_collection``."""
    return list(mongo_collection.find())
