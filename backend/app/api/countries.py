from app import app
from mongodb_helper import *

@app.get("/api/countries")
def get_countries():

    db = get_database()
    aggregate_countries_collection = db["aggregate.countries"]

    out = {}
    for country in aggregate_countries_collection.find():
        out[country["_id"]] = country["data"]

    return out 

@app.get("/api/countries/{country_name}")
def get_countries(country_name: str):

    db = get_database()
    aggregate_countries_collection = db["aggregate.countries"]

    out = aggregate_countries_collection.find_one({"_id": country_name})
    return out