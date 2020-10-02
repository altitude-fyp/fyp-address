from mongodb_helper import *

from app import constants

import pickle
def get_top_countries(countryname):
    cossim_matrix = pickle.load(open("pickled/top_countries_cossim_matrix.sav", "rb"))

    top3 = cossim_matrix[countryname][:3]

    return [{"name":name, "score":score, "flag":constants.COUNTRIES[name]["flag"]} for name,score in top3]


