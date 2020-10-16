import pickle
from app import app
from .analytics_helper.top_countries import *

@app.get("/api/analytics/top_countries/{country_name}")
def get_top_countries_(country_name: str):
    """
    input: country name
    output: top 3 similar countries
    """
    try:
        return {
            "status": "success",
            "top3": get_top_countries(country_name)
        }
    
    except Exception as err:
        return {
            "status": "failure",
            "error": str(err),
        }
    
@app.get("/api/analytics/npl_forecast")
def get_npl_forecast():
    """
    output: dict
        key = country name
        value = 1 or 0
            - 0 if country's NPL is predicted to fall the following year
            - 1 if country's NPL is predicted to rise the following year
    """
    return pickle.load(open("pickled/npl_binary_forecast.sav", "rb"))