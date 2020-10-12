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
from cleaner.worldbank_cleaner import clean_worldbank
from helper.combiner import *

dbpedia = pickle.load(open("pickled/dbpedia_countries.sav", "rb"))
wikipedia = pickle.load(open("pickled/wikipedia.sav", "rb"))
imf = pickle.load(open("pickled/imf.sav", "rb"))
worldbank = pickle.load(open("pickled/worldbank.sav", "rb"))

# cleaning all raw data sources
dbpedia = clean_dbpedia(dbpedia)
wikipedia = clean_wikipedia(wikipedia)
imf = clean_imf(imf)
worldbank = clean_worldbank(worldbank)

countries, charts, embeddings = combine(dbpedia, wikipedia, imf, worldbank)

from helper.db_insert import *

insert_into_db(data=countries, collection_name="aggregate.countries")
insert_into_db(data=charts, collection_name="aggregate.charts")
insert_into_db(data=embeddings, collection_name="aggregate.embeddings")

print("\ndone\n")