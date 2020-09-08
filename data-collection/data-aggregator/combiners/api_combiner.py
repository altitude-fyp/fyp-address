"""
contains combine_as_api_data, which combines all 3 data sources
    - output is meant for frontend to call 
    - human readability takes precedence over machine readability here
"""
from copy import deepcopy
from helper.nlp import *

def combine_as_api_data(countries, wikipedia, imf):
    
    countries = deepcopy(countries)

    for feature in wikipedia:

        print("Api data combiner: combining wikipedia feature with dbpedia countries", feature["name"])
        data = feature["data"]

        for row in data:
            
            wiki_country = row["country"]

            best_match, score = match(wiki_country, countries)

            if score > 0.85:
                countries[best_match][feature["name"]] = row

    for country_name, country_data in imf.items():

        print("Api data combiner: combining IMF data for", country_name, end=": ")

        best_match, score = match(country_name, countries)

        if score > 0.85:
            print("Best match found:", best_match)
            for k,v in country_data.items():
                countries[best_match][k] = v

        else:
            print("No match found")
    
    return countries