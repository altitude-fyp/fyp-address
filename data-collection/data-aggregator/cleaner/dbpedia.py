from common import *

dbpedia_countries_collection = db["dbpedia.countries"]

def get_dbpedia_countries():
    """
    returns cleaned dictionary representing dbpedia countries
        key = country name
        value = useful fields
    """

    def clean(text):
        """
            1. removes brackets
                eg. 1.345 (SGD) -> 1.345

        """

        def remove_brackets(text):
            for i,ch in enumerate(text):
                if ch in "{([":
                    return text[:i].strip()
            return text.strip()

        if type(text) == str:
            text = remove_brackets(text)
            try: return float(text)
            except: return text

        else:
            return [clean(i) for i in text]

    exceptions = {"geo:geometry"}

    countries = get_dbpedia_countries_raw()

    for country, info in countries.items():

        for k,v in info.items():
            if k not in exceptions:
                info[k] = clean(v)

    return countries



def get_dbpedia_countries_raw():
    """
    returns dict (raw)
        key = country name
        value = useful fields
    """
    countries = {j["_id"]: j["data"] for j in [i for i in dbpedia_countries_collection.find()]}
    
    # filtering features in dict "useful_fields"
    countries = {country: {k:v for k,v in info.items() if k in useful_fields} for country,info in countries.items()}
    
    return countries
    