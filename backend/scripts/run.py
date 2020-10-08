import os
from generate_constants import *

os.system("rm -rf pickled")
os.system("mkdir pickled")

generate_constants()

from generate_default_api import *
generate_default_api()