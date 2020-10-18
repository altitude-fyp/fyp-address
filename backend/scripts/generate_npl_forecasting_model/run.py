import os
import platform

if platform.system() == "Windows":
    ex = "python"
else:
    ex = "python3"

scripts = [
    "scripts/generate_npl_forecasting_model/preprocessing/run.py",
    "scripts/generate_npl_forecasting_model/train/run.py",
    "scripts/generate_npl_forecasting_model/predict/run.py",
]

for script in scripts:
    os.system(ex + " " + script)