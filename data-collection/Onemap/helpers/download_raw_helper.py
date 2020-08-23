import requests
import constants
import json

import os
from dotenv import load_dotenv
load_dotenv()

def get_data(url, area):
    response = requests.get(url, params={
        'token': os.getenv("ONEMAP_TOKEN"),
        'year': constants.YEAR,
        'planningArea': area        
    })
    # print(response.content)
    return json.loads(response.content)

def get_area_list():
    response = requests.get(constants.GET_PLANNING_AREA, params={
        'token': os.getenv("ONEMAP_TOKEN"),
        'year': constants.YEAR,
    })
    json_content = json.loads(response.content)
    area_list = []
    for area in json_content:
        area_list.append(area["pln_area_n"])
    return area_list