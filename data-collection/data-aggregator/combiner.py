from copy import deepcopy
from helper.nlp import *

def combine(dbpedia, wikipedia, imf):
    """
    input:
        dbpedia - dict representing country data from dbpedia
            {
                country1: data1,
                country2: data2
            }

        wikipedia - list of dicts representing table data from wikipedia
            [
                {table1 data},
                {table2 data}
            ]

        imf - dict representing country data from imf
            {
                country1: data1,
                country2: data2
            }
    """

    def get_dbpedia_imf_mappings(dbpedia, imf, threshold=0.85):
        """
        output: dict containing dbpedia-imf country mappings
            - country names are inconsistent in both dictionaries
            - pick only those who score > threshold
            - so that everything in final output will have data from both dbpedia and imf
        """
        out = {}
        for country in dbpedia:
            best_match, score = match(country, imf)

            if score > 0.85:
                out[country] = best_match
 
        return out

    dbpedia_imf_mappings = get_dbpedia_imf_mappings(dbpedia, imf)

    embeddings = {k:v for k,v in dbpedia.items() if k in dbpedia_imf_mappings}
    charts = {k:{} for k in dbpedia if k in dbpedia_imf_mappings}

    # combining embeddings with wikipedia data
    for feature in wikipedia:

        print("Combining with wikipedia tables:", feature["name"])
        data = feature["data"]

        for row in data:
            
            wiki_country = row["country"]
            best_match, score = match(wiki_country, dbpedia_imf_mappings)
            
            if score > 0.85:
                
                # inserting wiki data into embeddings
                main = feature["main"]
                if type(main) == str:
                    embeddings[best_match][feature["name"]] = row[main]

                elif type(main) == dict:
                    for key, display_name in main.items():
                        embeddings[best_match][display_name] = row[key]

    print()

    for country, imf_country in dbpedia_imf_mappings.items():

        print("Combining with IMF data: Matching", country)

        for imf_key, imf_value in imf[imf_country].items():
            
            # inserting imf data into embeddings
            latest = sorted([(k,v) for k,v in imf_value.items()], key=lambda x:x[0])[-1][-1]
            try: latest = float(latest)
            except: pass

            embeddings[country][imf_key] = latest

            # inserting imf data into charts
            charts[country][imf_key] = {k:float(v) for k,v in imf_value.items()}

    assert len(embeddings) == len(charts)

    return embeddings, charts







    