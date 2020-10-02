"""
this file contains all constants used in the application

    - all_countries is a dictionary
    
        key = country name
        value = {
            lat: latitude,
            lon :longitude,
            code: 2 letter country code,
            flag: link to country flag
        }
"""

import pickle

COUNTRIES = pickle.load(open("pickled/all_countries.sav", "rb"))