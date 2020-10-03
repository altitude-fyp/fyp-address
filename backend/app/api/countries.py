from app import app
from mongodb_helper import *
from pydantic import BaseModel
from collections import defaultdict
from typing import List

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
    countries = items

    data = {}

    coordinates = [{"lat":constants.COUNTRIES[country]["lat"], "long": constants.COUNTRIES[country]["lon"]} for country in countries]
    flags = [constants.COUNTRIES[country]["flag"] for country in countries]
    
    countries = {cname:get_country(cname) for cname in countries}

    top8cat = [
        "Gdp nominal", "Hdi", "Financial Development Index", "Consumer Price Index, All items",
        "Population total", "Gini", "Unemployment rate", "Life expectancy (overall)"
        ]

    top8 = [{"name":cat, "value":[cdata.get(cat, None) for cname, cdata in countries.items()]} for cat in top8cat]
    items = [{"name":fname, "value":[countries[cname][fname] for cname in countries]} for fname, fdata in countries["Singapore"].items()]

    data["coordinates"] = coordinates
    data["flag"] = flags
    data["filter"] = constants.COUNTRY_FEATURE_CATEGORIES
    data["top8"] = top8
    data["item"] = items

    return {
        "status": "success",
        "data": data
    }    