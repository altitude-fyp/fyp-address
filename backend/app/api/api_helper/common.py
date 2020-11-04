import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

def search_onemap_api(address):
    url = "https://developers.onemap.sg/commonapi/search"
    
    response = requests.get(url, params={
        'searchVal': address,
        'returnGeom': "Y",
        'getAddrDetails': "Y"        
    })

    print(response)
    
    return json.loads(response.content)

def get_planning_area_onemap(lat, lng):
    url = "https://developers.onemap.sg/privateapi/popapi/getPlanningarea"
    
    response = requests.get(url, params={
        'token': os.getenv("ONEMAP_TOKEN"),
        'lat': lat,
        'lng': lng        
    })

    print(response)
    
    return json.loads(response.content)