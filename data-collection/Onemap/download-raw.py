"""
Downloads raw onemap api data and stores in mongodb
"""
import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/onemap")])

from helpers.download_raw_helper import *
from constants import *
from mongodb_helper import *

if __name__ == "__main__":
    area_list = get_area_list()
    """
    { 
      _id: “aljunied”
       data:  {.  
            economicStatus: []
            religion: []
        }
    }
    """
    
    # Loop through area list
    data = {}
    for area in area_list:
        print(area)
        data_object = {}
        # Loop through API list
        for key, value in URL_LIST_POP_AREA.items():
            data_value = get_data(value, area)
            data_object[key] = data_value
            
        data[area] = data_object
        print("Finish writing " + str(area) + " data")
    
    final_data = {"_id": "Singapore", "data": data}
    mongo_upsert(data=final_data, collection_name="onemap", replacement_pattern={"_id": "Singapore"})
    print("Finish writing to MongoDB")