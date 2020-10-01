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
from helper.combiner import *

dbpedia = pickle.load(open("pickled/dbpedia_countries.sav", "rb"))
wikipedia = pickle.load(open("pickled/wikipedia.sav", "rb"))
imf = pickle.load(open("pickled/imf.sav", "rb"))

# cleaning all raw data sources
dbpedia = clean_dbpedia(dbpedia)
wikipedia = clean_wikipedia(wikipedia)
imf = clean_imf(imf)

countries, charts, embeddings = combine(dbpedia, wikipedia, imf)

from helper.db_insert import *

insert_into_db(data=countries, collection_name="test.aggregate.countries")
insert_into_db(data=charts, collection_name="test.aggregate.charts")
insert_into_db(data=embeddings, collection_name="test.aggregate.embeddings")

