#!/usr/bin/env python3
"""Listsdocuments"""
def list_all(mongo_collection):
    """Return documents"""
    documents = list(mongo_collection.find())
    return documents;
