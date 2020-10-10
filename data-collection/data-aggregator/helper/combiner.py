from copy import deepcopy
from helper.nlp import *
from helper.preprocessor import preprocess, check_preprocess

def combine(dbpedia, wikipedia, imf, worldbank):
    """
    input: dbpedia, wikipedia, imf and worldbank datasets
    output: aggregate.embeddings, aggregate.charts and aggregate.countries

        1. aggregate.countries
            - dbpedia and wikipedia data
            - for frontend's use

        2. aggregate.charts
            - imf data
            - for frontend's use to plot charts

        3. aggregate.embeddings
            - dbpedia, wikipedia and imf data
            - every value is a float
            - for developer use
    """

    def get_imf_dbpedia_mappings(dbpedia, imf, threshold=0.85):
        """
        output: dictionary where
                    key = imf country
                    value corresponding dbpedia country

            - country names are inconsistent, so this matches country naems 
                from different datasets
            - pick only countries where imf target variables are present 
        """

        t1 = "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Asset Quality, Non-performing Loans to Total Gross Loans, Percent"
        t2 = "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Capital Adequacy, Non-performing Loans Net of Provisions to Capital, Percent"

        out = {}
        unmapped = []

        for imf_cname, imf_cdata in imf.items():
            
            if t1 not in imf_cdata or t2 not in imf_cdata:
                continue

            best_dbpedia_cname, score = match(imf_cname, dbpedia)

            if score > threshold:
                out[imf_cname] = best_dbpedia_cname

            else:
                unmapped.append((imf_cname, best_dbpedia_cname, score))

        return out, unmapped

    def get_worldbank_dbpedia_mappings(dbpedia, worldbank, threshold=0.85):
        """
        output: dictionary where
                    key = imf country
                    value corresponding dbpedia country

            - country names are inconsistent, so this matches country naems 
                from different datasets
            - pick only countries where imf target variables are present 
        """

        t1 = "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Asset Quality, Non-performing Loans to Total Gross Loans, Percent"
        t2 = "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Capital Adequacy, Non-performing Loans Net of Provisions to Capital, Percent"

        out = {}
        unmapped = []

        for worldbank_cname, worldbank_cdata in worldbank.items():
            
            if t1 not in worldbank_cdata or t2 not in worldbank_cname:
                continue

            best_dbpedia_cname, score = match(worldbank_cname, dbpedia)

            if score > threshold:
                out[imf_cname] = best_dbpedia_cname

            else:
                unmapped.append((worldbank_cname, best_dbpedia_cname, score))

        return out, unmapped

    imf_dbpedia_mappings, unmapped_imf_countries = get_imf_dbpedia_mappings(dbpedia, imf)

    print("no. unmapped countries in IMF dataset:", len(unmapped_imf_countries))

    worldbank_dbpedia_mappings, unmapped_imf_countries = get_worldbank_dbpedia_mappings(dbpedia, worldbank)

    print("no. unmapped countries in Worldbank dataset:", len(unmapped_imf_countries))
    
    embeddings = {k:dbpedia[k] for k in imf_dbpedia_mappings.values()}
    charts = {k:{} for k in imf_dbpedia_mappings.values()}

    # combining embeddings with wikipedia data
    for feature in wikipedia:

        print("Combining with wikipedia tables:", feature["name"], " "*60, end="\r")
        data = feature["data"]

        for row in data:
            
            wiki_country = row["country"]
            best_match, score = match(wiki_country, imf_dbpedia_mappings.values())
            
            if score > 0.85:
                
                # inserting wiki data into embeddings
                main = feature["main"]
                if type(main) == str:
                    embeddings[best_match][feature["name"]] = row[main]

                elif type(main) == dict:
                    for key, display_name in main.items():
                        if key in row:
                            embeddings[best_match][display_name] = row[key]
                        else:
                            embeddings[best_match][display_name] = None

    embeddings = {cname: {k[0].upper() + k[1:]: v for k,v in cdata.items()} for cname,cdata in embeddings.items()}
    countries = deepcopy(embeddings)

    print("\ndone combining with wikipedia data\n")

    for imf_cname, dbpedia_cname in imf_dbpedia_mappings.items():

        for imfk, imfv in imf[imf_cname].items():

            imfv = {k:float(v) for k,v in imfv.items()}

            charts[dbpedia_cname][imfk] = imfv

            latest = sorted([(k,v) for k,v in imfv.items()], key=lambda x:x[0])[-1][-1]
            embeddings[dbpedia_cname][imfk] = latest

    for worldbank_cname, dbpedia_cname in worldbank_dbpedia_mappings.items():
    
        for worldbankk, worldbankv in worldbank[worldbank_cname].items():

            worldbankv = {k:float(v) for k,v in worldbankv.items()}

            charts[dbpedia_cname][worldbankk] = worldbankv

            latest = sorted([(k,v) for k,v in worldbankv.items()], key=lambda x:x[0])[-1][-1]
            embeddings[dbpedia_cname][worldbankk] = latest

    assert len(embeddings) == len(charts) and len(embeddings) == len(countries)

    countries = preprocess(countries)
    embeddings = preprocess(embeddings)

    check_preprocess(countries)
    check_preprocess(embeddings)

    return countries, charts, embeddings







    