from time import time
from app import app
from mongodb_helper import *
from pydantic import BaseModel
from collections import defaultdict
from typing import List
import pickle
from copy import deepcopy

from app import constants

class ItemList(BaseModel):
    countries: List[str]

def get_country_data(cname):
    db = get_database()
    out = db["aggregate.embeddings"].find_one({"_id": cname})["data"]
    return out


@app.get("/api/countries/metadata/{countries}")
def get_country_metadata_(countries):
    """
    returns country metadata: name, lat, lon, flag, country code for each country
    """
    return {cname: constants.COUNTRIES[cname] for cname in countries.split(",")}


@app.get("/api/countries/selectableFeatures/{countries}") # AKA filters
def get_selectable_features(countries):
    """
    returns all country features (categorised)
    """
    return constants.COUNTRY_FEATURE_CATEGORIES


@app.get("/api/countries/statistics/{countries}")
def get_country_statistics_(countries):
    """
    returns data (non-time-series) of all countries
    """
    return {cname: get_country_data(cname) for cname in countries.split(",")}




@app.get("/api/countries/list")
def get_country_list_():
    """
    Return a list of all countries sorted in aphabetical order
    """
    return {
        "status": "success",
        "data": {
            "items": sorted(list(constants.COUNTRIES.keys()))
        }
    }    

@app.post("/api/countries/")
def get_countries__(items:ItemList):
    """
    Return country data for frontend application 
    """
    countries = items.countries

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
    data["items"] = items

    features = [i for o in data["filter"] for i in o["value"]]
    features = {f:i for i,f in enumerate(features)}
    try: 
        data["items"].sort(key=lambda x:features[x["name"]])
    except:
        pass

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

        temp = countries_data[i]
        out = {"country": countries[i]}
        for k,v in temp.items():
            out[k] = v
        
        countries_data[i] = out

    return countries_data