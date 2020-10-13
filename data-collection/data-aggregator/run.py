"""
1. runs pull.py to pickle store all raw data
2. runs main.py to process and combine data, and store in mongodb

THIS IS TO BE RAN FROM THE DATA-COLLECTION DIRECTORY
"""

from pull import *
from main import *