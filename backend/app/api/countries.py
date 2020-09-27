from app import app
from mongodb_helper import *
from .constants import *

@app.get("/api/countries")
def get_countries_list():
  
    db = get_database()
    constant_collection = db["constant"]
    data = constant_collection.find_one({"_id": "continents"})

    out = {"status": "error", "data": {}}
    if data:
        out["status"] = "success"
        out["data"]["items"] = data["data"]
    return out

def format_countries_filter(data_dict):
    data_list = []
    for key, value in data_dict.items():
        data_list.append(key)
    return data_list


@app.get("/api/countries/{country_name}")
def get_countries_data(country_name: str):

    db = get_database()
    aggregate_countries_collection = db["aggregate.embeddings"]

    out = {"status": "error", "data": {}}
    data = aggregate_countries_collection.find_one({"_id": country_name})
    
    if data:
        result = format_countries_data(data["data"])
        coordinates = get_coordinates(country_name)
        out["status"] = "success"
        out["data"]["coordinates"] = coordinates[country_name]
        out["data"]["filter"] = get_filter_list()
        out["data"]["top8"] = result[1]
        out["data"]["items"] = result[0]
    return out

def format_countries_data(data_dict):
    data_list = []
    top8_list = []
    top8_filter = ["Gdp nominal", "Hdi", "Financial Development Index", "Consumer Price Index, All items",
                   "Population total", "Area total", "Unemployment rate", "Life expectancy (overall)"]
    master_list = get_master_filter_list()
    for item in master_list:
        obj = {}
        obj["name"] = item
        obj["value"] = data_dict[item]
        data_list.append(obj)

        if item in top8_filter:
            top8_list.append(obj)
    return [data_list, top8_list]

def get_coordinates(country_name):
    db = get_database()
    constant_collection = db["constant"]
    data = constant_collection.find_one({"_id": "coordinates"})
    return data["data"]