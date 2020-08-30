from app import app
from mongodb_helper import *

@app.get("/api/countries")
def get_countries():
    return {"countries": "all"}

@app.get("/api/countries/{country_name}")
def get_countries(country_name: str):
    return {"countries": country_name}