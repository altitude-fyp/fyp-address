from app import app
from mongodb_helper import *
import json

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

# DOESNT WORK
@app.get("/api/regions/{region_name}")
def get_regions_data(region_name: str):
    
    db = get_database()
    collection = db["onemap"]

    out = { "status": "error", "data": None }
    data = collection.find_one({"_id": region_name})

    if data:
        out["status"] = "success"
        out["data"] = data["data"]["population"]
    return out



# temporary
def get_region_polygon(region_name):
    db = get_database()

    out = db["onemap.polygons"].find_one({"_id": region_name})["data"]

    return {
        "name": region_name,
        "polygon": [{"lat": i[1], "lng": i[0]} for i in json.loads(out)["coordinates"][0][0]]
    }



# TEMPORARY
@app.get("/api/regions/polygons/{region_names}")
def get_region_polygons(region_names):
    out = []
    for name in region_names.split(","):
        try:
            out.append(get_region_polygon(name))
        except:
            pass
    
    return out
