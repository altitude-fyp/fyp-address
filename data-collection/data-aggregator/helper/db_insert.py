from helper.common import *

def insert_into_db(data, collection_name, tag=""):
    mongo_clear(collection_name)

    for country_name, country in data.items():
        print(tag, f"inserting {country_name} into mongodb")

        mongo_insert(
            data = {
                "_id": country_name,
                "data": country
            },
            collection_name=collection_name
        )
    