import os
from generate_constants import *

os.system("rm -rf pickled")
os.system("mkdir pickled")

os.system("python scripts/generate_constants/run.py")
os.system("python scripts/generate_country_similarity_matrix/run.py")