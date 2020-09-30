"""
inserts dbpedia page of every city and country found on wikipedia
"""
import sys
here = sys.path[0]
sys.path.append(here[:-len("dbpedia")]) 

from mongodb_helper import *
from helper import *

countries = get_countries()

data = {}

for country in countries:
    
    url = DBPEDIA_BASE + country.replace(" ", "_")
    
    print("scraping", country, "->", url, " "*50, end="\r")

    out = scrape(url)

    if len(out) >= 6:
        data[country] = out

print("\nfinished scraping\n")

COLLECTION_NAME = "dbpedia.countries"

mongo_clear(COLLECTION_NAME)

for cname, cdata in data.items():
    out = {
        "_id": cname,
        "data": cdata
    }

    print("inserting into mongodb:", cname, " "*50, end="\r")
    mongo_insert(out, COLLECTION_NAME)

print("\ndone")





