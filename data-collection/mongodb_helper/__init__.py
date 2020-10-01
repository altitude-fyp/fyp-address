"""
contains helper functions to CRUD to mongodb
"""

import os
from dotenv import load_dotenv
load_dotenv()

import pymongo

def get_database():
    """
        returns pymongo database object
    """
    return pymongo.MongoClient(os.getenv("MONGODB_CONNECTION_URL"))["main"]
    
def mongo_find_one(collection_name, find_options):
    """
    retrieves one entry from collection with collection_name with key
    """
    db = get_database()
    collection = db[collection_name]

    return collection.find_one(find_options)

def mongo_clear(collection_name):
    """
    empties collection
    """
    db = get_database()
    collection = db[collection_name]
    return collection.delete_many({})

def mongo_insert(data, collection_name):
    """
    inserts data into collection with collection_name
    """
    db = get_database()
    collection = db[collection_name]
    return collection.insert(data, check_keys=False)