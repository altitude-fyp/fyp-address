import requests
from bs4 import BeautifulSoup
import pandas as pd   

def get_private_list():
    #check URA private estates
    url = 'https://www.ura.gov.sg/realEstateIIWeb/transaction/search.action'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    rows = soup.select('option')

    rows = rows[127:-149]

    for i in range(len(rows)):
        rows[i] = (str(rows[i]).split(">")[1].split("<")[0])
    
    return rows

private_list = get_private_list()

#input: [{"POSTAL": "380105", "BUILDING": "HDB-GEYLANG EAST", "BLK_NO" : "105"}]
def check_property_type_list(address_entries, private_list):
    categories = {'HDB':0,'PRIVATE':0, 'OTHERS':0}
    
    for address_details in address_entries:
        if address_details['POSTAL'][-3:] == address_details['BLK_NO']:
            categories['HDB'] += 0
        elif address_details['BUILDING'] in private_list:
            categories['PRIVATE'] += 0
        else:
            categories['OTHERS'] += 0
    
    return categories

#input: {"POSTAL": "380105", "BUILDING": "HDB-GEYLANG EAST", "BLK_NO" : "105"}
def check_property_type(address, private_list):
    if address['POSTAL'][-3:] == address['BLK_NO']:
        return 'HDB'
    elif address['BUILDING'] in private_list:
        return 'PRIVATE'
    else:
        return 'OTHERS'