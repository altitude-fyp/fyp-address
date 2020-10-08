import pickle
from app import app
from .analytics_helper.top_countries import *

# UNUSED FOR NOW
@app.get("/api/analytics/top_features/{n}")
def get_top_features(n: int):
    """
    input: nothing
    output: top x features that are most highly correlated with each target variable
    """

    yname, modelname, model, score, weights = pickle.load(open("analytics/models/top_features.sav", "rb"))

    return {
        "yname": yname,
        "model name": modelname,
        "score": score,
        "weights": sorted(weights, key=lambda x:-x[-1]) [:int(n)]
    }

@app.get("/api/analytics/top_countries/{country_name}")
def get_top_countries_(country_name: str):
    """
    Get top 3 similar countries
    """
    try:
        return {
            "status": "success",
            "data": {
                "items": get_top_countries(country_name)
            }
        }
    
    except Exception as err:
        return {
            "status": "failure",
            "error": str(err),
        }
    