"""

Shared code for data-collection/dbpedia, data-collection/IMF and data-collection/IMF

to import without problems, use:

import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/<insert path name here>")])

in order to add "<whatever-path>/data-collection" into sys.path
"""


import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="../mongodb/.env")

import pymongo

def get_database(url):
    """
        returns pymongo database object
    """
    return pymongo.MongoClient(url)["main"]