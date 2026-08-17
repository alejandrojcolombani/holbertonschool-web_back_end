#!/usr/bin/env python3
"""Provide a helper for updating the topics taught by a school."""


def update_topics(mongo_collection, name, topics):
    """Set ``topics`` on every school document matching ``name``."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
    )
