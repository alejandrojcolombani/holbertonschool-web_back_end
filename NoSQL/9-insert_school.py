#!/usr/bin/env python3
"""Provide a helper for inserting a school document into MongoDB."""


def insert_school(mongo_collection, **kwargs):
    """Insert a document built from ``kwargs`` and return its identifier."""
    return mongo_collection.insert_one(kwargs).inserted_id
