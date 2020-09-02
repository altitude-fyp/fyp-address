"""
1. pulls raw data from dbpedia, wikipedia and IMF
2. pickle dump and store in pickled folder (gitignored)
3. subsequently, just need to pickle load the data from the pickled folder
    - much faster 

NOTE: this script is to be run from the data-collection directory
    - python3 data-aggregator/pull.py
"""

from helper.common import *
from time import time

db = get_database()

# if pickled not in data-collection, make pickled folder
if "pickled" not in os.listdir():
    os.system("mkdir pickled")

start = time()

print("\nPulling raw dbpedia.countries data")
dbpedia_countries_collection = db["dbpedia.countries"]
dbpedia_countries = {j["_id"]: j["data"] for j in [i for i in dbpedia_countries_collection.find()]}
    
cp1 = time(); print("Done! time taken:", cp1-start, "seconds\n")

print("Pulling raw wikipedia data")
wikiepdia_collection = db["wikipedia"]
wikipedia = [i for i in wikiepdia_collection.find()]

cp2 = time(); print("Done! time taken:", cp2-cp1, "seconds\n")

print("Pulling raw IMF data")
imf_collection = db["imf"]
imf = {j["_id"]: j["data"] for j in [i for i in imf_collection.find()]}

cp3 = time(); print("Done! time taken:", cp3-cp2, "seconds\n")

print("pickle dumping all raw datasets")
pickle.dump(dbpedia_countries, open("pickled/dbpedia_countries.sav", "wb"))
pickle.dump(wikipedia, open("pickled/wikipedia.sav", "wb"))
pickle.dump(imf, open("pickled/imf.sav", "wb"))

print("done - total time saved NOT waiting for data to load:", cp3-start, "seconds\n")
