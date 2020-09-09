# makes sure data-collection directory is in path
import sys
here = sys.path[0]
sys.path.append(here[:-len("data-aggregator")])

import os
import pickle

from mongodb_helper import *
