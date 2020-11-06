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
from helpers.clean_charts import *
from helpers.generate_summary import *

def insert_population_function(area, data):
    """
    function to be inserted into get_population_data function 
    so as to insert into db after every area is done pulling
    """
    print(f"inserting into onemap.raw: {area}" + " "*40, end="\r")
    mongo_insert({"_id":area, "data":data}, "onemap.raw")


if __name__ == "__main__":

    polygon_data = get_area_polygons()

    mongo_clear("onemap.polygons")
    for area, data in polygon_data.items():
        print(f"inserting into onemap.polygons: {area}" + " "*40, end="\r")
        mongo_insert({"_id":area, "data":data}, "onemap.polygons")

    print("\n")

    mongo_clear("onemap.raw")
    population_data = get_population_data(insert_population_function)

    print("\nCleaning onemap data\n")

    data = [i for i in get_database()["onemap"].find()]

    data = clean(data)
    print(data)
    mongo_clear("onemap")
    for i in data:
        print(f"inserting into onemap: {i['_id']}" + " "*40, end="\r")
        mongo_insert(i, "onemap")

    print("\nCleaning onemap data for charts\n")

    data = clean_charts(data)

    mongo_clear("onemap.charts")
    for i in data:
        print(f"inserting into onemap.charts: {i['_id']}" + " "*40, end="\r")
        mongo_insert(i, "onemap.charts")
    
    print("\n\ndone\n")

    print("generating onemap summary")

    summary = generate_summary(data)
    mongo_clear("onemap.summary")
    for o in summary:
        print("inserting into onemap.summary", o["_id"], " "*30, end="\r")
        mongo_insert(o, "onemap.summary")
    print("\n\ndone")