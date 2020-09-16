from app import app
from mongodb_helper import *

'''
/api/regions/<countryName>/<regionName>

Input: regionName
Output: region level data for 1 region

/api/regions/<countryName>

Input: nuthin
Output: region level data for all regions in 1 country

'''
@app.get("/api/regions")
def get_regions():

    db = get_database()
    constant_collection = db["constant"]

    out = { "status": "error", "data": None }
    # data = constant_collection.find_one({"_id": "country"})    
    # if data:
        # out["status"] = "success"
        # out["data"] = data["data"]

    out["status"] = "success"
    out["data"] = ["Newton", "Paya Lebar", "Bedok"]

    return out 


@app.get("/api/regions/{region_name}")
def get_regions_data(region_name: str):
    
    db = get_database()
    imf_collection = db["onemap"]

    out = { "status": "error", "data": None }
    data = imf_collection.find_one({"_id": country_name})

    if data:
        out["status"] = "success"
        out["data"] = data["data"]["population"]
    return out