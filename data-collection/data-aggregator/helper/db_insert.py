from helper.common import *

def insert_into_db(data, collection_name):
    mongo_clear(collection_name)

    for country_name, country in data.items():
        print(collection_name, f"inserting {country_name}", " "*50, end="\r")

        mongo_insert(
            data = {
                "_id": country_name,
                "data": country
            },
            collection_name=collection_name
        )
    
    print()
    