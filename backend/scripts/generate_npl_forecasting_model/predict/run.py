"""
1. picks best model out of models.sav
2. uses it to predict 2020 NPL
"""

print()
print("="*100)
print("Choosing the best performing model and using it to predict 2020 NPL using 2019 data")
print("="*100)
print()

# added to not print warnings
import warnings
warnings.filterwarnings('ignore')

from pick_best_model import *
model = pick_best_model()

import pandas as pd

data = pd.read_csv("scripts/generate_npl_forecasting_model/topredict.csv", sep="\t")

cnames = data.iloc[:,0]
x = data.iloc[:,1:]

from sklearn.preprocessing import MinMaxScaler

mmscaler = MinMaxScaler()
mmscaler.fit(x)
xmm = mmscaler.transform(x)

y_pred = model.predict(xmm)

out = {cname:pred for cname,pred in zip(cnames.values, y_pred)}

print(out)
print("\nno. of 0:", list(out.values()).count(0), "no. of 1:", list(out.values()).count(1))

import pickle
pickle.dump(out, open("pickled/npl_binary_forecast.sav", "wb"))

print("\noutput has been pickled in pickled/npl_binary_forecast.sav\n")
