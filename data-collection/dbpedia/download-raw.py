"""
Downloads raw dbpedia data and stores in mongodb 
    This script is meant to be run from the data-collection directory
"""

"""
adding to sys.path to import data-collection/mongodb_helper.py
"""
import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/dbpedia")])

from helpers.download_raw_helper import *
from mongodb_helper import *

SINGAPORE_URL = "http://dbpedia.org/page/Singapore"
AREAS_OF_SINGAPORE_URL = "http://dbpedia.org/page/Planning_Areas_of_Singapore"

if __name__ == "__main__":
    data = get_data(main_url=SINGAPORE_URL, areas_url=AREAS_OF_SINGAPORE_URL)

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



