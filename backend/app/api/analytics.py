from app import app

@app.get("/api/analytics/top_features")
def analytics_():
    """
    input: nothing
    output: top 10 features that are most highly correlated with each target variable

    """