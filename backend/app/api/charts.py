from app import app
from mongodb_helper import *

GRAPH_SHOWN = {
        "Consumer Price Index, All items" : "The Consumer Price Index provides a comprehensive means to benchmark buying habits of urban consumers.",
        "Financial Development Index": "The Financial Development Index provides a comprehensive means for economies to benchmark various aspects of their financial systems.", 
        "Financial Institutions Index": "The  Financial Institutions Index provides a comprehensive means for economies to benchmark various aspects of their financial institutions.", 
        "Financial Markets Index": "The  Financial Markets Index provides a comprehensive means for economies to benchmark various aspects of their financial markets."
    }

@app.get("/api/charts/{country_name}")
def get_chart_data(country_name: str):
  
    db = get_database()
    constant_collection = db["aggregate.charts"]
    data = constant_collection.find_one({"_id": country_name})
    out = {"status": "error", "data": {}}
    if data:
        result = format_chart_output(data["data"])
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
            for k,v in value.items():
                obj["years"].append(k)
                obj["value"].append(v)
            result.append(obj)
    return result

