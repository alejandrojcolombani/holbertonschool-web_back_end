#!/usr/bin/env python3
"""Provide a helper for finding schools that teach a given topic."""


def schools_by_topic(mongo_collection, topic):
    """Return all school documents whose topics include ``topic``."""
    return list(mongo_collection.find({"topics": topic}))
