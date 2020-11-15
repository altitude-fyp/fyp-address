from mongodb_helper import *

from app import constants
from copy import deepcopy

import pickle

def cosine_similarity(a,b):
    """
    input: 2 country vectors
    output: a float number between 0 and 1
        - the closer this number is to 1, the more "similar" the 2 country vectors are
        - vice verse: closer to 0 = not similar
    """

    def standardize(a,b):
        """
        makes sure every key is present in a and b
        """
        a = deepcopy(a)
        b = deepcopy(b)
        
        keys = set(list(a.keys()) + list(b.keys()))
        for k in keys:
            if k not in a:
                a[k] = 0
            if k not in b:
                b[k] = 0
        return a,b
    
    def dot(a,b):
        out = 0
        for k in a:
            out += a[k]*b[k]
        return out
    
    def magnitude(vector):
        out = 0
        for k,v in vector.items():
            out += v ** 2
        
        return out ** 0.5
    
    a,b = standardize(a,b)
    dotab = dot(a,b)
    maga, magb = magnitude(a), magnitude(b)
    
    out = dotab / maga / magb if 0 not in [maga, magb] else 0

    return out**8

def get_top_countries(countryname):
    cossim_matrix = pickle.load(open("pickled/country_similarity_matrix.sav", "rb"))
    top3 = cossim_matrix[countryname][:3]
    return [{"name":name, "score":score, "flag":constants.COUNTRIES[name]["flag"]} for name,score in top3]

def get_top_countries_for_api(countryname):
    cossim_matrix = pickle.load(open("pickled/country_similarity_matrix.sav", "rb"))
    top3 = cossim_matrix[countryname][:3]
    return [{ name:score } for name,score in top3]