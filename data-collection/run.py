import os

cmds = [
    "python IMF/run.py",
    "python dbpedia/run.py",
    "python Onemap/run.py",
    "python wikipedia/run.py"
    "python data-aggregator/run.py"
]

for cmd in cmds:
    os.system(cmd)
    