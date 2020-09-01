import sys
here = sys.path[0]
sys.path.append(here[:-len("data-aggregator")])
from mongodb_helper import *

db = get_database()

import pickle
from helper import *
from helper.nlp import *