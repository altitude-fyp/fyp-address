"""
Downloads raw onemap api data and stores in mongodb
"""
import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/onemap")])

from mongodb_helper import *

from helpers.population import *
from helpers.polygons import *
from helpers.clean import *

def insert_population_function(area, data):
    """
    function to be inserted into get_population_data function 
    so as to insert into db after every area is done pulling
    """
    print(f"inserting into onemap.raw: {area}" + " "*40, end="\r")
    mongo_insert({"_id":area, "data":data}, "onemap.raw")


if __name__ == "__main__":

    # polygon_data = get_area_polygons()

    # mongo_clear("onemap.polygons")
    # for area, data in polygon_data.items():
    #     print(f"inserting into onemap.polygons: {area}" + " "*40, end="\r")
    #     mongo_insert({"_id":area, "data":data}, "onemap.polygons")

    # print("\n")

    mongo_clear("onemap.raw")
    population_data = get_population_data(insert_population_function)

    print("\nCleaning onemap data\n")

    data = [i for i in get_database()["onemap.raw"].find()]
    data = clean(data)
    
    mongo_clear("onemap")
    for i in data:
        print(f"inserting into onemap: {i['_id']}" + " "*40, end="\r")
        mongo_insert(i, "onemap")
    
    print("\n\ndone\n")