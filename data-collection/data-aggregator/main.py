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
# from cleaner.imf_cleaner import clean_imf

from helper.combiner import combine

countries = pickle.load(open("pickled/dbpedia_countries.sav", "rb"))
wikipedia = pickle.load(open("pickled/wikipedia.sav", "rb"))
# imf = pickle.load(open("pickled/imf.sav", "rb"))

# cleaning all raw data sources
countries = clean_dbpedia(countries)
wikipedia = clean_wikipedia(wikipedia)
# imf = clean_imf(imf)

# """
# combining data sources
#     output: dictionary
#         key = country name
#         value = combination of dbpedia, wikipedia and imf data
# """

data = combine(countries, wikipedia, {})

for k,v in data.get("Singapore", {}).items():
    print(k, "==>", v)

# """
# inserting data into mongodb
# """


