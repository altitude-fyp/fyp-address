import platform
import os
from generate_constants import *

os.system("rm -rf pickled")
os.system("mkdir pickled")

commands = [
    "python3 scripts/generate_constants/run.py",
    "python3 scripts/generate_country_similarity_matrix/run.py"
]

for command in commands:
    """
    auto-detects platform used, as "python" is used in windows and "python3" is used otherwise
    """
    if platform.system() == "Windows":
        command = command.replace("python3", "python")

    os.system(command)

