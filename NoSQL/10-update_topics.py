#!/usr/bin/env python3
"""Update name, topics"""
def update_topics(mongo_collection, name, topics):
    """Update name, topics"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
    return doc
