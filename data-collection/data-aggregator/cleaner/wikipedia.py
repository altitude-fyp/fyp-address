from common import *

wikipedia_collection = db["wikipedia"]

def get_wikipedia_tables():
    """
    """
    raw = get_wikipedia_tables_raw()

    return raw


def get_wikipedia_tables_raw():
    """
    returns raw list of tables from wikipedia
    """
    wikipedia = [i for i in wikipedia_collection.find()]
    
    return wikipedia