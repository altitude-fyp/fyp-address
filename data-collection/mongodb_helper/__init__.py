"""
contains helper functions to CRUD to mongodb
"""

import os
from dotenv import load_dotenv
load_dotenv()

import pymongo

def get_database(url):
    """
        returns pymongo database object
    """
    return pymongo.MongoClient(url)["main"]

def mongo_upsert(data, collection_name, replacement_pattern):
    """
    upserts data into mongodb collection with collection_name
        - if data doesnt exist (based on repalcement_pattern), inserts
        - else if data exists, replaces
    """
    db = get_database(os.getenv("MONGODB_CONNECTION_URL"))
    collection = db[collection_name]

    result = collection.replace_one(
        replacement_pattern,
        data,
        upsert=True
    )

    print("Number of articles inserted/modified:", result.modified_count)

def mongo_find_one(collection_name, find_options):
    """
    retrieves one entry from collection with collection_name with key
    """
    db = get_database(os.getenv("MONGODB_CONNECTION_URL"))
    collection = db[collection_name]

    return collection.find_one(find_options)

