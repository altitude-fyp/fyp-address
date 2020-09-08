"""
contains combine_as_embeddings function, which combines dbpedia, wikipedia and imf data into embedings
    - in an embedidng, every value shall be a float, string, or null
    - no dicts, lists or nested dicts etc
    - for machine readability
"""
from copy import deepcopy
from helper.nlp import *

def combine_as_embeddings(countries, wikipedia, imf):
    """
        input: cleaned data from dbpedia.countries, wikipedia and imf
        output: dictionary
            key = country anme
            value = dictionary representing combined cleaned data from all 3 sources
    """
    countries = deepcopy(countries)
    for feature in wikipedia:
        
        print("Embeddings combiner: combining wikipedia feature with dbpedia countries:", feature["name"])
        data = feature["data"]

        for row in data:

            wiki_country = row["country"]

            best_match, score = match(wiki_country, countries)

            if score > 0.85:

                main = feature["main"]

                if type(main) == str:
                    countries[best_match][feature["name"].replace(" ", "_")] = row[main]

                elif type(main) == list:
                    for k in main:
                        k_cleaned = feature["name"] + "_" + k
                        k_cleaned = k_cleaned.replace(" ", "_")
                        countries[best_match][k_cleaned] = row[k]

    for country_name, country_data in imf.items():

        print("Embeddings combiner: combining IMF data for", country_name, end=": ")
    
        best_match, score = match(country_name, countries)

        if score > 0.85:
            print("Best match found:", best_match)
            for k,v in country_data.items():
                countries[best_match][k] = v[-1]["@OBS_VALUE"]

        else:
            print("No match found")

    return countries
