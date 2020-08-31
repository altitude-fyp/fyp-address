"""
fetch data from all sources, clean, combine and store
"""

import sys
here = sys.path[0]
sys.path.append(here[:-len("data-aggregator")])
from mongodb_helper import *

db = get_database()

dbpedia_countries_collection = db["dbpedia.countries"]
wikipedia_collection = db["wikipedia"]
imf_collection = db["imf"]

countries = {j["_id"]: j["data"] for j in [i for i in dbpedia_countries_collection.find()]}
wikipedia = [i for i in wikipedia_collection.find()]
imf = {j["_id"]: j["data"] for j in [i for i in imf_collection.find()]}

"""
pickling for development purposes as pulling data takes 5 seconds
"""
# import pickle
# pickle.dump((countries, wikipedia), open("pickled/data.sav", "wb"))
# countries, wikipedia = pickle.load(open("pickled/data.sav", "rb"))

from helper import *
from helper.nlp import *

# filter only useful features in countries (see helper/__init__.py)
countries = {country: {k:v for k,v in info.items() if k in useful_fields} for country,info in countries.items()}

# appending metadata from wikipedia
for meta in wikipedia:
    data = meta["data"]
    for row in data:
        ckey, score = match(row["country"], countries)
        if score > 0.8:
            countries[ckey][meta["name"]] = row

# appending IMF data

for country, dataflows in imf.items():
    print(country)
    for dataflow_name, indicators in dataflows.items():
        ckey, score = match(country, countries)
        if score > 0.8:
            countries[ckey][dataflow_name] = indicators

mongo_clear("aggregate.countries")

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