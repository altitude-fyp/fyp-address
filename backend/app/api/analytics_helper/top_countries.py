from mongodb_helper import *

import pickle
def get_top_countries(countryname):
    cossim_matrix = pickle.load(open("analytics_scripts/pickled/top_countries_cossim_matrix.sav", "rb"))

    top3 = cossim_matrix[countryname][:3]
    flags = get_flags()

    return [{"name":name, "score":score, "flag":flags[name]} for name,score in top3]

def get_flags():
    db = get_database()
    constant_collection = db["constant"]
    data = constant_collection.find_one({"_id": "flag"})
    return data["data"]
