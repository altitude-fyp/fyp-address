"""
create pickled folder
create venv named env
activate env
pip3 install dependencies

remind user to add in stuff into the .env manually
remind user to run scripts/run.py after .env
"""

import os

COMMANDS = [
    "mkdir pickled",
    "python3 -m venv env",
    "source env/bin/activate",
    "pip3 install -r requirements.txt"
]

for cmd in COMMANDS:
    os.system(cmd)

print("IMPORTANT: remember to create your .env file")
print("IMPORTANT: remember to run scripts/run.py after you have created your .env file")
