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
    onemap_collection = db["onemap"]

    out = { "status": "error", "data": None }
    data = onemap_collection.find()    
    if data:
        planning_areas = [area["_id"].title() for area in data]
        out["status"] = "success"
        out["data"] = planning_areas

    return out 


@app.get("/api/regions/{regions}")
def get_regions_chart_data(region_name: str):
    
    db = get_database()
    onemap_chart_collection = db["onemap.charts"]

    countries = countries.split(",")
    
    combined_raw_data_list = []
    for country_name in countries:
        data = onemap_chart_collection.find_one({"_id": country_name})
        combined_raw_data_list.append(data)

    out = { "status": "error", "data": None }

    if data:
        out["status"] = "success"
        out["data"] = data["data"]["population"]
    return out