import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../mongodb/.env")

import requests
from helper import extract_urls, jsonify_dbpedia_url

SINGAPORE_URL = "http://dbpedia.org/data/Singapore.json"

def get_data(url=SINGAPORE_URL):
    """
        input: url to singapore's dbpedia article page in JSON format
        
        output: dictionary representing singapore's dbpedia page
            contains:
                1. singapore dbpedia url (key) -> singapore dbpedia JSON page

    """

    singapore = requests.get(url).json()

    return singapore

def get_database(url):
    """
        returns pymongo database object
    """
    return pymongo.MongoClient(url)["main"]


if __name__ == "__main__":
    data = get_data()
    print(data)
    



