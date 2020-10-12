from helpers.common import *
from mongodb_helper import *

def get_top_npl_countries():
    db = get_database()
    npl_data = {}

    for i in db["aggregate.embeddings"].find():
        if "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Asset Quality, Non-performing Loans to Total Gross Loans, Percent" in i["data"]:
            npl_data[i["_id"]] = i["data"]["Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Asset Quality, Non-performing Loans to Total Gross Loans, Percent"]

    pickle.dump(npl_data, open("pickled/top_npl_countries.sav", "wb"))

    return sorted(npl_data.items(), key=lambda kv: kv[1])[:20]

def get_all_npl_data():
    db = get_database()

    embeddings_collection = db["imf.quarter"]
    pickle.dump(embeddings_collection, open("pickled/all_npl_data.sav", "wb"))
    
    return 1

def get_npl_data(countryname):

    all_npl_data = pickle.load("pickled/all_npl_data.sav", "rb")

    for i in all_npl_data.find():
        if i["_id"] == countryname:
            return i["data"]
 
    return 0


get_top_npl_countries()

get_all_npl_data()

print(get_npl_data("Singapore"))