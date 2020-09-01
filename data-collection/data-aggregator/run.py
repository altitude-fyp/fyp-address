"""
fetch data from all sources, clean, combine and store
"""

from common import *
from cleaner.dbpedia import * 
from cleaner.wikipedia import *

print("pulling dbpedia countries")
countries = get_dbpedia_countries()

print("pulling wikipedia tables")
wikipedia = get_wikipedia_tables()

print("pulling imf data")
imf_collection = db["imf"]
imf = {j["_id"]: j["data"] for j in [i for i in imf_collection.find()]}

print("appending wikipedia table data into respective countries")
for meta in wikipedia:
    data = meta["data"]
    for row in data:
        ckey, score = match(row["country"], countries)
        if score > 0.8:
            countries[ckey][meta["name"]] = row

print("appending IMF data")
for country, dataflows in imf.items():
    for dataflow_name, indicators in dataflows.items():
        ckey, score = match(country, countries)
        if score > 0.8:
            countries[ckey][dataflow_name] = indicators

print("clearing mongodb database")
mongo_clear("aggregate.countries")

print("inserting country-level data into mongodb database")
for country, data in countries.items():
    result = mongo_insert(
        {   
            "_id": country,
            "data": data
        },

        collection_name="aggregate.countries"
    )

    print(f"Added {country} into aggregate.countries: {result}")

print("done")