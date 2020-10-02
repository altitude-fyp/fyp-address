"""
this script computes the cosine similarity matrix of every country
vs every other country

"""

from helpers.common import *
from mongodb_helper import *
from copy import deepcopy

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
    
    return dotab / maga / magb if 0 not in [maga, magb] else 0

def compute_top_countries_matrix():
    db = get_database()
    embeddings_collection = db["test.aggregate.embeddings"]

    embeddings = {}
    for i in embeddings_collection.find():
        embeddings[i["_id"]] = i["data"]

    out = {cname:[] for cname in embeddings}
    
    for cname, cdata in embeddings.items():
        for cname2, cdata2 in embeddings.items():
            score = cosine_similarity(cdata, cdata2)
            if cname != cname2:
                out[cname].append((cname2, score))

    for cname, scores in out.items():
        scores.sort(key=lambda x:-x[-1])

    pickle.dump(out, open("scripts/pickled/top_countries_cossim_matrix.sav", "wb"))

    print("finished computing top countries cosine similarity matrix")