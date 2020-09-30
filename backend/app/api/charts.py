from app import app
from mongodb_helper import *
from .constants import *
from typing import List
from pydantic import BaseModel
from collections import defaultdict
from statsmodels.tsa.ar_model import AutoReg

class ItemList(BaseModel):
    countries: List[str]

GRAPH_SHOWN = {
        "Consumer Price Index, All items" : "The Consumer Price Index provides a comprehensive means to benchmark buying habits of urban consumers.",
        "Financial Development Index": "The Financial Development Index provides a comprehensive means for economies to benchmark various aspects of their financial systems.", 
        "Financial Institutions Index": "The  Financial Institutions Index provides a comprehensive means for economies to benchmark various aspects of their financial institutions.", 
        "Financial Markets Index": "The  Financial Markets Index provides a comprehensive means for economies to benchmark various aspects of their financial markets."
    }

@app.post("/api/charts/")
def get_chart_data(items: ItemList):
    db = get_database()
    chart_collection = db["aggregate.charts"]
    out = {"status": "error", "data": {}}

    combined_raw_data_list = []
    for country_name in items.countries:
        data = chart_collection.find_one({"_id": country_name})["data"]
        combined_raw_data_list.append(data)

    dd = defaultdict(list)
    for d in combined_raw_data_list:
        for key, value in d.items():
            dd[key].append(value)

    if data:
        result = format_chart_output(dd)
        out["status"] = "success"
        out["data"]["items"] = result
    return out

def format_chart_output(data_dict):
    result = []
    for key, value in data_dict.items():
        if key in GRAPH_SHOWN:
            obj = {"title": "", "description": "", "years": [], "value": []}
            obj["title"] = key
            obj["description"] = GRAPH_SHOWN[key]
            for country in value:
                country = extrapolate(country)
                year_list = []
                value_list = []
                for k,v in country.items():
                    year_list.append(k)
                    value_list.append(v)
                # obj["years"].append(year_list)
                obj["years"] = year_list
                obj["value"].append(value_list)
            result.append(obj)
    return result

def extrapolate(data, desired=[i for i in range(2000,2020)], lag=1):
    
    data = {int(k):float(v) for k,v in data.items()}
    
    def get_forward():
        fstart = len(data)
        fend = len(data) + max(desired) - max(data.keys())-1

        forward_model = AutoReg(list(data.values()),lag)
        forward_res = forward_model.fit()
        forward = forward_model.predict(forward_res.params, start=fstart, end=fend)
        
        return list(forward)

    def get_backward():
        bstart = len(data)
        bend = len(data) + min(data.keys()) - min(desired) -1
        
        print(bstart, bend)

        backward_model = AutoReg(list(data.values())[::-1],lag)
        backward_res = backward_model.fit()
        backward = backward_model.predict(backward_res.params, start=bstart, end=bend)
        
        return list(backward)[::-1]
    
    forward, backward = [], []
    
    if max(data.keys()) < max(desired):
        forward = get_forward()
        
    if min(data.keys()) > min(desired):
        backward = get_backward()
        
    temp = backward + list(data.values()) + forward
    
    return {k:v for k,v in zip(desired, temp)}