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


@app.get("/api/countries/selectableFeatures/") # AKA filters
def get_selectable_features():
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
        "countries": sorted(list(constants.COUNTRIES.keys()))
    }    

@app.get("/api/countries/csv/{countries}")
def get_countries_csv_(countries):
    countries = countries.split(",")
    countries_data = [get_country_data(cname) for cname in countries]
    
    for i in range(len(countries)):

        temp = countries_data[i]
        out = {"country": countries[i]}
        for k,v in temp.items():
            out[k] = v
        
        countries_data[i] = out

    return countries_data
