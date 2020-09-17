from app import app
from mongodb_helper import *

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

@app.get("/api/filter/{country_name}")
def get_filter_list(country_name: str):
    db = get_database()
    aggregate_countries_collection = db["aggregate.embeddings"]
    
    out = { "status": "error", "data": {} }
    data = aggregate_countries_collection.find_one({"_id": country_name})
    if data:
        result = format_countries_filter(data["data"])
        out["status"] = "success"
        out["data"]["items"] = result

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

    out = { "status": "error", "data": {} }
    data = aggregate_countries_collection.find_one({"_id": country_name})

    if data:
        result = format_countries_data(data["data"])
        out["status"] = "success"
        out["data"]["items"] = result
    return out

def format_countries_data(data_dict):
    data_list = []
    for key, value in data_dict.items():
        obj = {}
        obj["name"] = key
        obj["value"] = value
        data_list.append(obj)
    return data_list