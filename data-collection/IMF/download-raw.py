"""
Downloads raw imf data and stores in mongodb 
    This script is meant to be run from the data-collection directory
"""

"""
adding to sys.path to import data-collection/mongodb_helper.py
"""
import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/imf")])

from helpers.download_raw_helper import *
from mongodb_helper import *

here = sys.path[0]
sys.path.append(here[:len(here)-len("/imf")])

if __name__ == "__main__":

    #retrieve all dataflow mapping names
    dataflow_mapping = get_dataflow_mapping()

    #retrieve all data parameters
    common_data = get_common_data()

    #retrieve all common countries (243)
    common_countries = get_npl_countries(common_data)

    #retrieve all country data
    all_country_data = get_batch_country_data(common_countries)

    #retrieve all indicators names
    indicator_mapping = get_indicator_mapping(dataflow_mapping, common_data)

    #find common all indicators and map to indicator names
    common_mapping = get_common_mapping(indicator_mapping, all_country_data)

    # convert all indicator_ids to indicator names
    converted_all_country_data = convert_all_country_data(indicator_mapping, all_country_data)

    countries_to_add = converted_all_country_data.keys()

    for country in countries_to_add:
        data = converted_all_country_data[country]

        data = {"_id": country, "data": data}

        mongo_upsert(data=data, collection_name="imf", replacement_pattern={"_id": country})