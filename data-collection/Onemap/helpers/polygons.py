import os
import requests
from helpers.common import *

def get_area_polygons():
    """
    gets polygons (list of all latlon coordinates) of all planning areas in singapore
    """
    endpoint = "https://developers.onemap.sg/privateapi/popapi/getAllPlanningarea?token=" + os.getenv("ONEMAP_TOKEN")

    raw = requests.get(endpoint).json()
    out = {}

    for item in raw:
        k = item["pln_area_n"].lower()
        v = item["geojson"]
        out[k] = v
    
    return out