import pickle
from app import app
from .analytics_helper.top_countries import *

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
def get_top_countries(country_name: str):
    out = {"status": "error", "data": {}}
    data = top_countries(country_name)
    if data:
        out["status"] = "success"
        out["data"]["items"] = data
    return out