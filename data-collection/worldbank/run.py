"""
Downloads raw worldbank data and stores in mongodb 
    This script is meant to be run from the data-collection directory
"""

"""
adding to sys.path to import data-collection/mongodb_helper.py
"""

import sys

here = sys.path[0]
sys.path.append(here[:len(here)-len("/worldbank")])

from helpers.download_raw_helper import *
from mongodb_helper import *

if __name__ == "__main__":
    
    COLLECTION_NAME = "worldbank"
    mongo_clear(COLLECTION_NAME)
    all_data = get_worldbank_data()

    for cname, cdata in all_data.items():
        out = {
        "_id": cname,
        "data": cdata
        }

        print("inserting into mongodb:", cname, " "*50, end="\r")
        mongo_insert(out, COLLECTION_NAME)

        print("\ndone")