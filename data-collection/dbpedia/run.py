"""
inserts dbpedia page of every city and country found on wikipedia
"""
import sys
here = sys.path[0]
sys.path.append(here[:-len("dbpedia")]) 

from mongodb_helper import *
from helper import *

countries_and_cities = get_countries_and_cities()

# clear everyting in dbpedia.countries collection
mongo_clear("dbpedia.countries")

for country, cities in countries_and_cities:

    try:
        assert len(country) > 0
        country = country.replace(" ", "_")
        print("="*150)
        print("parsing country:", country)
        print("="*150)

        country_data = parse_dbpedia_page(DBPEDIA_BASE + country)

        print(country, " --> data length:", len(country_data))
        
        mongo_upsert(
            data = {"_id": country, "data": country_data},
            collection_name="dbpedia.countries",
            replacement_pattern={"_id": country}
        )

    except Exception as err:
        print(f"ERROR parsing country {country}:", str(err))
            


