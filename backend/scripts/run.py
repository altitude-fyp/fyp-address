import os
from top_countries import *
from generate_constants import *
from generate_default_api import *

os.system("mkdir pickled")

compute_top_countries_matrix()
generate_constants()
generate_default_api()
