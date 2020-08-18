"""
PYMONGO DOCUMENTATION LINK: https://pymongo.readthedocs.io/en/stable/
"""

from dotenv import load_dotenv
load_dotenv()

import os
import pymongo

def get_database(url):
    """
        input: connection_url (remember to create your .env file)
        output: database object representing our main database

        note: we still need to get the collections inside the database
        eg
    """
    client = pymongo.MongoClient(url)
    return client["main"]

CONNECTION_URL = os.getenv("CONNECTION_URL")

db = get_database(CONNECTION_URL)

test = db["testCollection"]

for i in test.find({}):
    print(i)
    
