#!/usr/bin/env python3
"""Update school name, topics"""
def update_topics(mongo_collection, name, topics):
    """Update"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
