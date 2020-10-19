import pickle
"""
1. takes time series data from aggregate.charts
2. preprocesses it (fill null, remove irrelevant etc)
3. converts output data into csv
"""

print()
print("="*100)
print("NPL forecasting model: preprocessing")
print("="*100)
print()

from extrapolate import extrapolate

import sys
here = sys.path[0]
sys.path.append(here[:-len("/scripts/generate_npl_forecasting_model/preprocessing")])

from mongodb_helper import *

db = get_database()
t1 = "Bank nonperforming loans to total gross loans (%)"

raw = {}
for i in db["aggregate.charts"].find():
    raw[i["_id"]] = i["data"]

data = {}

"""
select countries to put into data dictionary
    - only countries with target variable + more than 5 years of data
"""

for cname, co in raw.items():
    
    if t1 in co and len(co[t1]) > 8:
        
        data[cname] = co
                
"""
some code to make sure autoregression does not get out of hand
"""
temp = []
for cname, co in data.items():
    for val in co[t1].values():
        temp.append(val)

print("min and max of original npl data:", min(temp), max(temp))


"""
remove time series data if less than 5 years available
"""

for cname, co in data.items():
    
    data[cname] = {fname: fo for fname, fo in co.items() if len(fo) > 5}

    
"""
remove features present in less than 85% of data
"""

d = {}

for cname, co in data.items():
    
    for fname, fo in co.items():
        
        if fname not in d:
            d[fname] = 1
        else:
            d[fname] += 1

THRESHOLD = int(0.85*len(data))

keep = set([fname for fname, n in d.items() if n >= THRESHOLD])

for cname, co in data.items():
    
    data[cname] = {fname: fo for fname, fo in co.items() if fname in keep}

pickle.dump(data, open("pickled/autoregressed_country_data.sav", "wb"))
"""
2-way autoregression to standardize time-series data first from 2000-2019
after this step, all values should be length 20
"""

for cname, co in data.items(): 
    for fname, fo in co.items():
        
        if fname == t1:
            co[fname] = extrapolate(fo, restrict=True)
            continue
        
        co[fname] = extrapolate(fo)


"""
compute average for each feature first
"""

avg = {fname:[] for fname in keep}

for fname in keep:
    for cname, co in data.items():
        
        if fname not in co:
            continue
        
        avg[fname].append(co[fname])
        
for fname, fos in avg.items():
    
    out = {year:sum([fo[year] for fo in fos])/20 for year in range(2000,2020)}
    avg[fname] = out

"""
making all features in keep appear in all countries
"""
d = {}
for cname, co in data.items():
        
    keys = set(co.keys())
    missing = keep - keys
    
    for fname in missing:
        co[fname] = avg[fname]
        
        if fname not in d:
            d[fname] = 1
            
        else:
            d[fname] += 1

print("no. of countries:", len(data))
print("no. features to keep:", len(keep))

"""
checking that autoregression doesnt go crazy
"""

temp = []
for cname, co in data.items():
    for val in co[t1].values():
        temp.append(val)

print("NEW min and max of original npl data after autoregression:", min(temp), max(temp))


"""
testing if every feature is present in every country in data, and if every value has years 2000-2019
"""

for cname, co in data.items():
    
    assert len(set(co.keys()) - keep) == 0
    
    for fname, fo in co.items():
        
        assert len(fo) == 20

"""
converting preprocessed data in csv format
"""

out = []

for cname, co in data.items():
    
    for year in range(2000,2019):
        
        row = {}
        
        row["npl"] = co[t1][year]
        row["npl_next"] = co[t1][year+1]
        
        for fname, fo in co.items():
            
            if fname == t1:
                continue
                
            row[fname] = fo[year]
        
        out.append(row)

import pandas as pd

csv = pd.DataFrame(out)

csv.to_csv("scripts/generate_npl_forecasting_model/npl.csv", index=False, sep="\t")

print("\ntraining data has been saved as npl.csv in scripts/generate_npl_forecasting_model/npl.csv\n")

"""
getting test data for 2019 data
    NOTE: this is not in the train dataset as 2020 data is unavailable -> no target variable
"""

LATEST_YEAR = max(data["Singapore"][t1].keys())

print("latest year:", LATEST_YEAR)

out = []

for cname, co in data.items():

    temp = {"countryname": cname}

    for fname, fo in co.items():

        if fname == t1:
            continue

        temp[fname] = fo[LATEST_YEAR]
        
    out.append(temp)

out = pd.DataFrame(out)
out.to_csv("scripts/generate_npl_forecasting_model/topredict.csv", index=False, sep="\t")

print(f"\ndata from {LATEST_YEAR} has been saved as scripts/generate_npl_forecasting_model/topredict.csv in scripts\n")