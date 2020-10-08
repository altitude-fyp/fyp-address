"""
Downloads raw imf data and stores in mongodb 
    This script is meant to be run from the data-collection directory
"""

"""
adding to sys.path to import data-collection/mongodb_helper.py
"""
import sys
from helpers.download_raw_helper import *
from mongodb_helper import *

here = sys.path[0]
sys.path.append(here[:len(here)-len("/imf")])


if __name__ == "__main__":

    all_mapping = dictionary_mapping(get_dataflow_parameters())

    npl_countries = get_npl_countries()

    print(npl_countries)
    
    all_data = get_data(chosen_indicators, 'A' , npl_countries)

    converted = convert_dictionary(all_data, all_mapping)

    countries_to_add = converted.keys()

    print(countries_to_add)

    for country in countries_to_add:
        data = converted[country]

        data = {"_id": country, "data": data}

        mongo_upsert(data=data, collection_name="imf", replacement_pattern={"_id": country})