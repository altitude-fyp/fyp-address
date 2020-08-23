import requests
import constants
import json

def get_data(url, area):
    response = requests.get(url, params={
        'token': constants.TOKEN,
        'year': constants.YEAR,
        'planningArea': area        
    })
    # print(response.content)
    return json.loads(response.content)

def get_area_list():
    response = requests.get(constants.GET_PLANNING_AREA, params={
        'token': constants.TOKEN,
        'year': constants.YEAR,
    })
    json_content = json.loads(response.content)
    area_list = []
    for area in json_content:
        area_list.append(area["pln_area_n"])
    # print(area_list)
    return response