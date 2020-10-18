from copy import deepcopy
from helper.nlp import *
from helper.preprocessor import preprocess, check_preprocess

def combine(dbpedia, wikipedia, imf, worldbank):
    """
    input: dbpedia, wikipedia, imf and worldbank datasets
    output: aggregate.embeddings, aggregate.charts and aggregate.countries

        1. aggregate.countries (frontend use) - dbpedia + wikipedia
        2. aggregate.charts (frontend use) - imf + worldbank
        3. aggregate.embeddings (analytics use) - dbpedia + wikipedia + imf + worldbank
    """

    def get_valid_countries(dbpedia, imf, worldbank, threshold=0.85):
        """
        returns list of tuples, each of length 3
            - (dbpedia_country_name, imf_country_name, worldbank_country_name)
            - country is valid only if present in all 3 data sources
        """

        out = []

        for dbpedia_cname in dbpedia:
            
            best_imf_cname, best_imf_score = match(dbpedia_cname, imf)
            best_worldbank_cname, best_worldbank_score = match(dbpedia_cname, worldbank)

            if best_imf_score > threshold and best_worldbank_score > threshold:
                out.append((dbpedia_cname, best_imf_cname, best_worldbank_cname))

        return out

    def combine_dictionaries(*dictionaries):
        out = {}
        for d in dictionaries:
            for k,v in d.items():
                out[k] = v
        return out

    valid_countries = get_valid_countries(dbpedia, imf, worldbank)
    countries = {dbpedia_cname: deepcopy(dbpedia[dbpedia_cname]) for dbpedia_cname, _, __ in valid_countries}
    
    print()

    # combining dbpedia with wikipedia data
    for table in wikipedia:
        print("Combining with wikipedia:", table["name"], " "*60, end="\r")
    
        tdata = table["data"]

        for row in tdata:
            
            best, score = match(row["country"], countries)

            if score < 0.85: continue

            if type(table["main"]) == str:
                countries[best][table["name"]] = row[table["main"]]

            elif type(table["main"]) == dict:
                for key, display_name in table["main"].items():
                    
                    if key in row:
                        countries[best][display_name] = row[key]
                    
                    else:
                        countries[best][display_name] = None
        
    embeddings = deepcopy(countries)
    charts = {}

    print("\nCombining with imf and worldbank data\n")

    for dbpedia_cname, imf_cname, worldbank_cname in valid_countries:

        dbpedia_cdata = dbpedia[dbpedia_cname]
        imf_cdata = imf[imf_cname]
        worldbank_cdata = worldbank[worldbank_cname]

        charts[dbpedia_cname] = combine_dictionaries(imf_cdata, worldbank_cdata)

        for imfk, imfv in imf_cdata.items():
            embeddings[dbpedia_cname][imfk] = sorted(imfv.items(), key=lambda x:x[0])[-1][-1]

        for wbk, wbv in worldbank_cdata.items():
            embeddings[dbpedia_cname][wbk] = sorted(wbv.items(), key=lambda x:x[0])[-1][-1]


    return countries, charts, embeddings
