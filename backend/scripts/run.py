import os
from top_countries import *
from generate_constants import *

os.system("mkdir pickled")

compute_top_countries_matrix()
generate_constants()
