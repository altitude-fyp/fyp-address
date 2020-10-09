"""
Downloads raw worldbank data and stores in mongodb 
    This script is meant to be run from the data-collection directory
"""

"""
adding to sys.path to import data-collection/mongodb_helper.py
"""
import sys
from helpers.download_raw_helper import *
from mongodb_helper import *

here = sys.path[0]
sys.path.append(here[:len(here)-len("/worldbank")])


if __name__ == "__main__":

    all_data = get_worldbank_data()

    countries_to_add = all_data.keys()

    print(countries_to_add)

    for country in countries_to_add:
        data = converted[country]

        data = {"_id": country, "data": data}

        mongo_upsert(data=data, collection_name="worldbank", replacement_pattern={"_id": country})