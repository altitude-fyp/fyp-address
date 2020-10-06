"""
Downloads raw onemap api data and stores in mongodb
"""
import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/onemap")])

from helpers.download_raw_helper import *
from constants import *
from mongodb_helper import *

def get_area_polygons():
    """
    gets polygons (list of all latlon coordinates) of all planning areas in singapore
    """
    endpoint = "https://developers.onemap.sg/privateapi/popapi/getAllPlanningarea?token=" + os.getenv("ONEMAP_TOKEN")

    print("Getting polygon data")

    raw = requests.get(endpoint).json()
    out = {}

    for item in raw:
        k = item["pln_area_n"].lower()
        v = item["geojson"]
        out[k] = v
    
    return out

def get_population_data():
    """
    gets economic data about singaporeans, segregated by area eg. orchard, seragoon, aljunied etc
    """

    print("Getting population data")

    area_list = get_area_list()

    data = {}

    print(area_list)

    for area in area_list:
        area = area.lower()

        data_object = {}
        # Loop through API list
        for key, value in URL_LIST_POP_AREA.items():
            data_value = get_data(value, area)
            data_object[key] = data_value
        
        data[area] = data_object
        print("Finish pulling " + str(area) + " data")
    
    return data

if __name__ == "__main__":
    
    data = {
        "_id": "Singapore",

        "data": {
            # "polygons": get_area_polygons(),
            "population": get_population_data()
        }

    }

    mongo_upsert(data=data, collection_name="onemap", replacement_pattern={"_id": "Singapore"})

    print("\nFinish writing to MongoDB\n")