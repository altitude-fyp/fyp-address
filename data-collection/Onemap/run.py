"""
Downloads raw onemap api data and stores in mongodb
"""
import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/onemap")])

from mongodb_helper import *

from helpers.population import *
from helpers.polygons import *

def insert_population_function(area, data):
    """
    function to be inserted into get_population_data function 
    so as to insert into db after every area is done pulling
    """
    print(f"inserting into onemap: {area}" + " "*40, end="\r")
    mongo_insert({"_id":area, "data":data}, "onemap")


if __name__ == "__main__":

    polygon_data = get_area_polygons()

    mongo_clear("onemap.polygons")
    for area, data in polygon_data.items():
        print(f"inserting into onemap.polygons: {area}" + " "*40, end="\r")
        mongo_insert({"_id":area, "data":data}, "onemap.polygons")

    print("\n")

    mongo_clear("onemap")
    population_data = get_population_data(insert_population_function)

    print("\ndone\n")
    
