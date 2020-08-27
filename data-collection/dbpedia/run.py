"""
inserts dbpedia page of every city and country found on wikipedia
"""
import sys
here = sys.path[0]
sys.path.append(here[:-len("dbpedia")]) 

from mongodb_helper import *
from helper import *

countries_and_cities = get_countries_and_cities()

for country, cities in countries_and_cities:

    try:
        assert len(country) > 0
        print("="*150)
        print("parsing country:", country)
        print("="*150)

        country_data = parse_dbpedia_page(DBPEDIA_BASE + country)
        
        mongo_upsert(
            data = {"_id": country, "data": country_data},
            collection_name="dbpedia.countries",
            replacement_pattern={"_id": country}
        )

    except Exception as err:
        print(f"ERROR parsing country {country}:", str(err))

    for city in cities:
        try:
            assert len(city) > 0
            print("parsing city:", city)

            city_data = parse_dbpedia_page(DBPEDIA_BASE + city)
            city_data["country"] = country

            mongo_upsert(
                data = {"_id": city, "data": city_data},
                collection_name="dbpedia.cities",
                replacement_pattern={"_id": city}
            )

        except Exception as err:
            print(f"ERROR parsing city {city}:", str(err))

