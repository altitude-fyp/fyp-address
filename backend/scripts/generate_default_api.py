"""
this script generates the default api that is called by frontend
and stores it in the pickled folder
"""


import sys
here = sys.path[0]
sys.path.append(here[:-len("scripts")])

from app import app
from fastapi.testclient import TestClient

def generate_default_api():
    
    print("generating default api for POST /api/countries/ and POST /api/charts/", end="")

    client = TestClient(app)

    r = client.post(
        "/api/countries/",
        headers={},
        json={"countries": ["Singapore"]}
    )

    countries = r.json()

    r = client.post(
        "/api/charts/",
        headers={},
        json={"countries": ["Singapore"]}
    )

    charts = r.json()

    import pickle

    pickle.dump(countries, open("pickled/default_post_api_countries.sav", "wb"))
    pickle.dump(charts, open("pickled/default_post_api_charts.sav", "wb"))

    print(" - finished")