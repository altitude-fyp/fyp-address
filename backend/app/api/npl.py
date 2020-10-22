from app import app
from mongodb_helper import *
from typing import List
from pydantic import BaseModel
from collections import defaultdict
from statsmodels.tsa.ar_model import AutoReg
from time import time
import pickle
from .analytics_helper.npl_countries_features import *

class ItemList(BaseModel):
    countries: List[str]

GRAPH_SHOWN = {
        "Bank nonperforming loans to total gross loans (%)" : " Bank nonperforming loans to total gross loans are the value of nonperforming loans divided by the total value of the loan portfolio (including nonperforming loans before the deduction of specific loan-loss provisions). The loan amount recorded as nonperforming should be the gross value of the loan as recorded on the balance sheet, not just the amount that is overdue."}

@app.get("/api/analytics/npl_charts/")
def get_chart_data(items: ItemList):

    starttime = time()

    db = get_database()
    chart_collection = db["worldbank"]
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
        result = format_chart_output(dd, items.countries)
        out["status"] = "success"
        out["data"]["items"] = result

    endtime = time()

    out["time taken"] = float(endtime-starttime)
    
    return out

def format_chart_output(data_dict, countries_list):
    result = []
    for key, value in data_dict.items():
        if key in GRAPH_SHOWN:
            obj = {"title": "", "description": "", "countries": [], "years": [], "value": []}
            obj["title"] = key
            obj["description"] = GRAPH_SHOWN[key]
            obj["countries"] = countries_list
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

@app.get("/api/analytics/sorted_npl_data/")
def get_sorted_npl_data():
    """
    output: sorted countries by non performing loans
    """
    starttime = time()

    db = get_database()

    chart_collection = db["worldbank"]

    npl_data = {}

    for i in db["aggregate.embeddings"].find():
        if "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Asset Quality, Non-performing Loans to Total Gross Loans, Percent" in i["data"]:
            npl_data[i["_id"]] = i["data"]["Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Asset Quality, Non-performing Loans to Total Gross Loans, Percent"]

    sorted_npl_data = sorted(npl_data.items(), key=lambda kv: kv[1])

    sorted_npl_data_list = []

    for country,npl in sorted_npl_data:
        sorted_npl_data_list.append({"name": country, "value": npl})

    try:
        return {
            "status": "success",
            "items": sorted_npl_data_list
        }
    
    except Exception as err:
        return {
            "status": "failure",
            "error": str(err),
        }


@app.get("/api/analytics/npl_country_features/")
def get_sorted_npl_data(countryname):
    """
    output: get top 10 features correlating to non performing loans
    """
    starttime = time()

    try:
        return {
            "status": "success",
            "items": get_npl_country_npl_features(countryname)
        }
    
    except Exception as err:
        return {
            "status": "failure",
            "error": str(err),
        }


