"""
Cleans raw dbpedia data and stores in mongodb
    This script is meant to be run from the data-collection directory
"""

"""
adding to sys.path to import data-collection/mongodb_helper.py
"""
import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/dbpedia")])

from helpers.clean_helper import *
from mongodb_helper import *
