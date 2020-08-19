"""
Downloads raw dbpedia data and stores in mongodb 

This script is meant to be run from the backend/data-collection directory
    eg. python dbpedia/run.py
"""

"""
adding to sys.path to import data-collection/mongodb_helper.py
"""
import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/data-collection/dbpedia")])

from mongodb.mongodb_helper import *
import requests

SINGAPORE_URL = "http://dbpedia.org/data/Singapore.json"

def get_data(url=SINGAPORE_URL):
    """
        input: url to singapore's dbpedia article page in JSON format
        
        output: dictionary representing singapore's dbpedia page
            contains:
                1. singapore dbpedia url (key) -> singapore dbpedia JSON page

    """

    singapore = requests.get(url).json()

    return singapore

if __name__ == "__main__":
    data = get_data()

    db = get_database(os.getenv("MONGODB_CONNECTION_URL"))
    dbpedia_collection = db["dbpedia"]

    """
        replace_one with usert=True
            - replaces if exists else inserts
    """
    result = dbpedia_collection.replace_one(
        {   "_id": "Singapore" },    
        
        {
            "_id": "Singapore",
            "data": str(data)
        },

        upsert=True
    )

    print("number of entries inserted/modified:",result.modified_count)



