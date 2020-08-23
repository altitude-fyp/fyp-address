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
    # area_list = get_area_list()
    """
    { 
      _id: “aljunied”
       data:  {.  
            economicStatus: []
            religion: []
        }
    }
    """

    area_list = ["BEDOK"]

    # Loop through area list
    for area in area_list:
        data_object = {}

        # Loop through API list
        for key, value in URL_LIST_POP_AREA.items():
            data_value = get_data(value, area)
            data_object[key] = data_value
        data = {"_id": area, "data": data_object}
        
        # Upsert to MongoDB
        mongo_upsert(data=data, collection_name="onemap", replacement_pattern={"_id": area})
    
    print(data)

            
