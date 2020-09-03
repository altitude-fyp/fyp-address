"""
contains combine_as_api_data, which combines all 3 data sources
    - output is meant for frontend to call 
    - human readability takes precedence over machine readability here
"""

from helper.nlp import *

def combine_as_api_data(countries, wikipedia, imf):
    
    for feature in wikipedia:

        print("Api data combiner: combining wikipedia feature with dbpedia countries", feature["name"])
        data = feature["data"]

        for row in data:
            
            wiki_country = row["country"]

            best_match, score = match(wiki_country, countries)

            if score > 0.85:
                countries[best_match][feature["name"]] = row

        """
        insert imf code here after mr wan is done with his code
        """
    
    return countries