import requests
import json
# import os
# from dotenv import load_dotenv
# load_dotenv()

def search_onemap_api(address):
    url = "https://developers.onemap.sg/commonapi/search"
    
    response = requests.get(url, params={
        'searchVal': address,
        'returnGeom': "N",
        'getAddrDetails': "Y"        
    })

    print(response)
    
    return json.loads(response.content)

