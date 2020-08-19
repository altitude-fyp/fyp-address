"""
contains helper functions to CRUD to mongodb
"""

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="../mongodb/.env")

import pymongo

def get_database(url):
    """
        returns pymongo database object
    """
    return pymongo.MongoClient(url)["main"]