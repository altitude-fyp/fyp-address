"""
runs all scripts in the analytics folder
"""

import os

if "models" not in os.listdir("analytics"):
    os.system("mkdir analytics/models")

print(os.listdir("analytics"))