import pickle
from app import app

@app.get("/api/analytics/top_features/{n}")
def analytics_(n: int):
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