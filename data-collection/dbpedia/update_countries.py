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

def mongo_upsert(data, collection_name, replacement_pattern):
    """
    upserts data into mongodb collection with collection_name
        - if data doesnt exist (based on repalcement_pattern), inserts
        - else if data exists, replaces
    """
    db = get_database()
    collection = db[collection_name]

    return collection.replace_one(
        replacement_pattern,
        data,
        upsert=True
    )
    
def mongo_find_one(collection_name, find_options):
    """
    retrieves one entry from collection with collection_name with key
    """
    db = get_database()
    collection = db[collection_name]

    return collection.find_one(find_options)

country_list = []

with open("citibank_countries.txt") as f:
    for line in f:
        country = line.strip().split("\n")
        country_list.append(country[0])
print(country_list)

mongo_upsert(
            data = {"_id": "country", "data": sorted(country_list)},
            collection_name="constant",
            replacement_pattern={"_id": "country"}
        )