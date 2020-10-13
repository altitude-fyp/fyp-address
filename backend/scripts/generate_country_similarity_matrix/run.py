import sys
here = sys.path[0]

sys.path.append(here[:-len("/scripts/generate_country_similarity_matrix")])

from mongodb_helper import *
from copy import deepcopy
import pickle

from cosine_similarity import cosine_similarity

def compute_top_countries_matrix():

    db = get_database()
    embeddings_collection = db["aggregate.embeddings"]

    embeddings = {}
    for i in embeddings_collection.find():

        cname = i["_id"]
        co = {k:v for k,v in i["data"].items() if type(v) in [float, int]} # ensure no null or invalid values

        embeddings[cname] = co

    out = {cname:[] for cname in embeddings}
    
    for cname, cdata in embeddings.items():

        print("computing cosine similarity score for", cname, " "*40, end="\r")

        for cname2, cdata2 in embeddings.items():

            score = cosine_similarity(cdata, cdata2)
            if cname != cname2:
                out[cname].append((cname2, score))

    for cname, scores in out.items():
        scores.sort(key=lambda x:-x[-1])

    pickle.dump(out, open("pickled/country_similarity_matrix.sav", "wb"))

if __name__ == "__main__":

    print("Generating country cosine similarity matrix\n")
    
    compute_top_countries_matrix()
    
    print("\n\ndone\n")