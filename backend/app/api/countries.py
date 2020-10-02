from app import app
from mongodb_helper import *
from .constants import *
from pydantic import BaseModel
from collections import defaultdict
from typing import List

from app import constants

class ItemList(BaseModel):
    countries: List[str]

@app.get("/api/countries/")
def get_countries_():
    """
    returns a list of all countries (in mongodb) sorted in aphabetical order
    """
    return sorted(list(constants.COUNTRIES.keys()))

def format_countries_filter(data_dict):
    data_list = []
    for key, value in data_dict.items():
        data_list.append(key)
    return data_list


@app.post("/api/countries/")
def get_countries_data(items: ItemList):
    db = get_database()
    aggregate_countries_collection = db["aggregate.embeddings"]
    coordinates = get_coordinates()
    flag = get_flag()
    out = {"status": "error", "data": {}}

    combined_raw_data_list = []
    coordinates_list = []
    flag_list= []
    for country_name in items.countries:
        data = aggregate_countries_collection.find_one({"_id": country_name})["data"]
        combined_raw_data_list.append(data)
        coordinates_list.append(coordinates[country_name])
        flag_list.append(flag[country_name])

    dd = defaultdict(list)
    for d in combined_raw_data_list:
        for key, value in d.items():
            dd[key].append(value)

    if data:
        result = format_countries_data(dd)
        out["status"] = "success"
        out["data"]["coordinates"] = coordinates_list
        out["data"]["flag"] = flag_list
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

def get_coordinates():
    db = get_database()
    constant_collection = db["constant"]
    data = constant_collection.find_one({"_id": "coordinates"})
    return data["data"]

def get_flag():
    db = get_database()
    constant_collection = db["constant"]
    data = constant_collection.find_one({"_id": "flag"})
    return data["data"]