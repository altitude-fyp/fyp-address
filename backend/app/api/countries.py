from time import time
from app import app
from mongodb_helper import *
from pydantic import BaseModel
from collections import defaultdict
from typing import List
import pickle

from app import constants

class ItemList(BaseModel):
    countries: List[str]

@app.get("/api/countries/")
def get_countries_():
    """
    Return a list of all countries sorted in aphabetical order
    """
    return {
        "status": "success",
        "data": {
            "items": sorted(list(constants.COUNTRIES.keys()))
        }
    }    

def get_country(cname):
    db = get_database()
    out = db["test.aggregate.embeddings"].find_one({"_id": cname})["data"]
    
    return out

@app.post("/api/countries/")
def get_countries__(items:ItemList):
    """
    Return country data for frontend application 
    """
    countries = items.countries

    # if input countries == ["Singpaore"] (the default), returns pickled object
    if len(countries) == 1 and countries[0] == "Singapore":
        try:
            starttime = time()
            out = pickle.load(open("pickled/default_post_api_countries.sav", "rb"))
            endtime = time()

            out["time taken"] = float(endtime-starttime)
            return out
        except: pass

    starttime = time()

    data = {}

    coordinates = [{"lat":constants.COUNTRIES[country]["lat"], "long": constants.COUNTRIES[country]["lon"]} for country in countries]
    flags = [constants.COUNTRIES[country]["flag"] for country in countries]
    
    countries = {cname:get_country(cname) for cname in countries}

    top8cat = [
        "Gdp nominal", "Hdi", "Financial Development Index", "Consumer Price Index, All items",
        "Population total", "Gini", "Unemployment rate", "Life expectancy (overall)"
    ]

    top8 = [{"name":cat, "value":[cdata.get(cat, None) for cname, cdata in countries.items()]} for cat in top8cat]
    items = [{"name":fname, "value":[countries[cname][fname] for cname in countries]} for fname, fdata in list(countries.values())[0].items()]

    data["coordinates"] = coordinates
    data["flag"] = flags
    data["filter"] = constants.COUNTRY_FEATURE_CATEGORIES
    data["top8"] = top8
    data["item"] = items

    endtime = time()

    return {
        "status": "success",
        "time taken": float(endtime-starttime),
        "data": data
    }    

@app.post("/api/csv/")
def get_csv_data(items:ItemList):
    countries = items.countries
    countries_data = [get_country(cname) for cname in countries]
    for i in range(len(countries)):
        countries_data[i]["country"] = countries[i]
    return countries_data