from app import app
from mongodb_helper import *
from collections import defaultdict

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

@app.get("/api/charts/regions/{regions}")
def get_regions_chart_data(regions):
    
    db = get_database()
    onemap_chart_collection = db["onemap.charts"]
    
    regions = regions.split(",")

    combined_raw_data_list = []
    for region in regions:
        data = onemap_chart_collection.find_one({"_id": region.lower()})["data"]
        combined_raw_data_list.append(data)

    out = {"status": "error", "data": {}}

    dd = defaultdict(list)
    for d in combined_raw_data_list:
        for key, value in d.items():
            dd[key].append(value)
            
    if data:
        combined_formated_data = format_chart_output(dd, regions)
        
        # Pre-define maps to show on frontend
        glance_tab = ["Economic Status", "Population Age Group", "Type of Dwelling Household", "Household Monthly Income", "Industry", "Tenancy"]
        economy_tab = ["Economic Status", "Household Monthly Income", "Income From Work", "Industry", "Occupation"]
        society_tab = ["Population Age Group", "Ethnic Group", "Spoken At Home", "Marital Status", "Language Literate", "Religion"]
        household_tab = ["Household Size", "Household Structure", "Type of Dwelling Household", "Tenancy", "Type of Dwelling Pop", "Education Attending"]
        
        out["status"] = "success"
        out["data"]["At a glance"] = [chart_data for chart_data in combined_formated_data if chart_data["title"] in glance_tab]
        out["data"]["Economy"] = [chart_data for chart_data in combined_formated_data if chart_data["title"] in economy_tab]
        out["data"]["Society"] = [chart_data for chart_data in combined_formated_data if chart_data["title"] in society_tab]
        out["data"]["Household"] = [chart_data for chart_data in combined_formated_data if chart_data["title"] in household_tab]
    return out

def format_chart_output(data_dict, regions_list):
    result = []
    for key, value in data_dict.items():
        obj = {"title": "", "regions": [], "years": [], "value": []}
        obj["title"] = key
        obj["regions"] = [region.title() for region in regions_list]
        for country in value:
            year_list = []
            value_list = []
            for k,v in country.items():
                year_list.append(k)
                value_list.append(v)
            obj["years"] = year_list
            obj["value"].append(value_list)
        result.append(obj)
            
    return result

def get_regions_data(regions):
    """
        Input: 1 region in Singapore
        Output: Region data
    """
    db = get_database()
    onemap_chart_collection = db["onemap"]
    
    if len(regions) > 1:
        regions = regions.split(",")
        combined_raw_data = {}
        for region in regions:
            data = onemap_chart_collection.find_one({"_id": region.lower()})["data"]
            combined_raw_data[region] = data

    combined_raw_data = onemap_chart_collection.find_one({"_id": region.lower()})["data"]

    out = {"status": "error", "data": {}}

    if data:
        out["status"] = "success"
        out["data"] = combined_raw_data

    return out