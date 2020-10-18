"""
THIS IS TO BE RAN FROM THE DATA-COLLECTION DIRECTORY
    - python data-aggregator/pull.py

1. pulls raw data from dbpedia, wikipedia and IMF
2. pickle dump and store in pickled folder (gitignored)
3. subsequently, just need to pickle load the data from the pickled folder
    - much faster 

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

print("Pulling raw Worldbank data")
worldbank_collection = db["worldbank"]
worldbank = {j["_id"]: j["data"] for j in [i for i in worldbank_collection.find()]}

cp4 = time(); print("Done! time taken:", cp4-cp3, "seconds\n")

print("pickle dumping all raw datasets")
pickle.dump(dbpedia_countries, open("pickled/dbpedia_countries.sav", "wb"))
pickle.dump(wikipedia, open("pickled/wikipedia.sav", "wb"))
pickle.dump(imf, open("pickled/imf.sav", "wb"))
pickle.dump(worldbank, open("pickled/worldbank.sav", "wb"))

print("done - total time saved NOT waiting for data to load:", cp4-start, "seconds\n")
