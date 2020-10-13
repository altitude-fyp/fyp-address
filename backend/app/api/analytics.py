import pickle
from app import app
from .analytics_helper.top_countries import *

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
    