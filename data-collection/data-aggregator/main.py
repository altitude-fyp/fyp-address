"""
1. pickle loads data from dbpedia, wikipedia and IMF
2. cleans and combines all data into final data object
    {
        country_name1: country_object1,
        country_name2: country_object2
    }
3. inserts into embeddings.countries mongodb collection

"""
from helper.common import *

from cleaner.dbpedia_cleaner import clean_dbpedia
from cleaner.wikipedia_cleaner import clean_wikipedia
from cleaner.imf_cleaner import clean_imf

# from combiners.embeddings_combiner import combine_as_embeddings
# from combiners.api_combiner import combine_as_api_data

from combiner import *

countries = pickle.load(open("pickled/dbpedia_countries.sav", "rb"))
wikipedia = pickle.load(open("pickled/wikipedia.sav", "rb"))
imf = pickle.load(open("pickled/imf.sav", "rb"))

# cleaning all raw data sources
countries = clean_dbpedia(countries)
wikipedia = clean_wikipedia(wikipedia)
imf = clean_imf(imf)

sg = countries["Singapore"]
for k,v in sg.items():
    print(k, v)

exit()

embeddings, charts = combine(countries, wikipedia, imf)

from helper.db_insert import *

insert_into_db(data=embeddings, collection_name="test.embeddings.countries", tag="EMBEDDINGS")
print("done inserting embeddings data into mongodb\n")

insert_into_db(data=charts, collection_name="test.aggregate.charts", tag="CHARTS")
print("done inserting embeddings data into mongodb\n")
