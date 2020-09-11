from app import app
from mongodb_helper import *

# Get list of countries
@app.get("/api/countries")
def get_countries_list():

    db = get_database()
    constant_collection = db["constant"]

    out = { "status": "error", "data": None }
    data = constant_collection.find_one({"_id": "country"})
    print(data)
    if data:
        out["status"] = "success"
        out["data"] = data["data"]
    return out 

@app.get("/api/countries/{country_name}")
def get_countries_data(country_name: str):

    db = get_database()
    aggregate_countries_collection = db["aggregate.countries"]

    out = { "status": "error", "data": None }
    data = aggregate_countries_collection.find_one({"_id": country_name})

    if data:
        out["status"] = "success"
        out["data"] = data["data"]

    return out