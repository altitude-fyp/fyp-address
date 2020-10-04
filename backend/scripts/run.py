import os
from top_countries import *
from generate_constants import *


os.system("rm -rf pickled")
os.system("mkdir pickled")


generate_constants()
compute_top_countries_matrix()

from generate_default_api import *
generate_default_api()