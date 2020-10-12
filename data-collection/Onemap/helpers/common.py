import requests
import json
from helpers.constants import *

import os
from dotenv import load_dotenv
load_dotenv()

def get_data(url, area, year="2015"):

    response = requests.get(url, params={
        'token': os.getenv("ONEMAP_TOKEN"),
        'year': year,
        'planningArea': area        
    })
    
    return json.loads(response.content)

