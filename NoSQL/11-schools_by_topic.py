#!/usr/bin/env python3
"""List topic"""
def schools_by_topic(mongo_collection, topic):
    """Find topic"""
    return list(mongo_collection.find({ "topics": topic }));
