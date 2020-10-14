"""
picks best model from models.sav
"""

import pandas as pd

data = pd.read_csv("scripts/generate_npl_forecasting_model/npl.csv", sep="\t")
y = data.iloc[:,:2]
x = data.iloc[:,2:]

# creating variable "increase" - whether next years's NPL is higher than current year
y["increase"] = [1 if j>i else 0 for i,j in zip(y["npl"], y["npl_next"])]

from sklearn.preprocessing import MinMaxScaler

mmscaler = MinMaxScaler()
mmscaler.fit(x)
xmm = mmscaler.transform(x)

import pickle

models = pickle.load(open("scripts/generate_npl_forecasting_model/models/models.sav", "rb"))

from sklearn.metrics import accuracy_score

def pick_best_model():

    print("individual performance of each of 5 models tested on entire dataset\n")

    name, best_model, best_score = None, None, 0

    for modelname, model in models.items():

        y_pred = model.predict(xmm)

        score = accuracy_score(y_pred, y.loc[:, "increase"])

        print(modelname, " "*(50-len(modelname)), "accuracy score:", round(score,4))

        if score > best_score:
            name = modelname
            best_score = score
            best_model = model

    print("\nBest model:", name, "with an accuracy score of", round(best_score, 4), "\n")

    return best_model
