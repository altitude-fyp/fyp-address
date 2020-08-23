"""
Downloads raw imf data and stores in mongodb 
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

here = sys.path[0]
sys.path.append(here[:len(here)-len("/imf")])

if __name__ == "__main__":
    data = get_data(country = 'Singapore')

    data = {"_id": "Singapore", "data": data}

    mongo_upsert(data=data, collection_name="imf", replacement_pattern={"_id": "Singapore"})