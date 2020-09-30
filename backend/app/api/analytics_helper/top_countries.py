from .common import *
from mongodb_helper import *

import pandas as pd

from copy import deepcopy

def cosine_similarity(a,b):
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
    
    return dotab / maga / magb if 0 not in [maga, magb] else 0


def top_countries(countryname):
    #query current datasets
    db = get_database()
    embeddings_countries_collection = db["aggregate.embeddings"]

    embeddings = {}
    for row in embeddings_countries_collection.find():
        country = row["_id"]
        data = row["data"]
        embeddings[country] = data

    df = pd.DataFrame(embeddings)

    country_data = df.to_dict()
    country_data = sorted(country_data.items(), key=lambda x: x[0])
    country_data

    out = {}

    for cname,cvalue in country_data:
        out[cname] = {}
        for dname,dvalue in country_data:
            out[cname][dname] = cosine_similarity(cvalue,dvalue)
        out[cname] = sorted(out[cname].items(), key=lambda x: x[1],reverse=True)[1:4]

    countries_similarity = dict(out[countryname])

    country_list = countries_similarity.keys()

    similar_features = {}
    for country in country_list:
        df5 = df[[countryname,country]].T
        country_data = df5.to_dict()
        country_data = sorted(country_data.items(), key=lambda x: x[0])
        country_data.append(('Final', {countryname: 1, country: 1}))
        country_data = dict(country_data)
        for cname,cvalue in country_data.items():
            out[cname] = {}
            for dname,dvalue in country_data.items():
                if cname == dname:
                    pass
                else:
                    out[cname][dname] = cosine_similarity(cvalue,dvalue)
            out[cname] = sorted(out[cname].items(), key=lambda x: x[1],reverse=True)[1:10]
        similar_features[country] = dict(out['Final'])
    
    response_output = []

    for country,similarity_score in countries_similarity.items():
        response_output.append({"name": country, "score": similarity_score, "value": list(similar_features[country].keys())})


    return response_output



print(top_countries('Singapore'))