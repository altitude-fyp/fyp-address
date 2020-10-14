"""
1. takes csv file converted by preprocess/run.py
2. trains model

model
- input: country's features for certain year
- output: boolean value
    - whether country's NPL rises or falls for the following year

5 best performing models
    1. NuSVC kernel="rbf"
    2. NuSVC kernel="poly"
    3. RandomForestClassifier criterion="gini"
    4. RandomForestClassifier criterion="entropy"
    5. KNeighborClassifier n_neighbors=1
"""

print()
print("="*100)
print("training NPL models")
print("="*100)
print()

import warnings
warnings.filterwarnings('ignore')

import pandas as pd

data = pd.read_csv("scripts/generate_npl_forecasting_model/npl.csv", sep="\t")

y = data.iloc[:,:2]
x = data.iloc[:,2:]

# creating variable "increase" - whether next years's NPL is higher than current year
y["increase"] = [1 if j>i else 0 for i,j in zip(y["npl"], y["npl_next"])]

# printing out proportion of 0s and 1s
y_ = [i for i in y["increase"]]
print("no. of 0:", y_.count(0), "/", len(y_), "proportion:", y_.count(0)/len(y_))
print("no. of 1:", y_.count(1), "/", len(y_), "proportion:", y_.count(1)/len(y_))
print()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

mmscaler = MinMaxScaler()
mmscaler.fit(x)
xmm = mmscaler.transform(x)

from sklearn.svm import NuSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

def train(x, y, Model, kwargs={}):
    
    model = Model(**kwargs)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    
    return model, score

model_metadata = [
    ("NuSVC kernel=rbf", NuSVC, {"kernel": "rbf"}),
    ("NuSVC kernel=poly", NuSVC, {"kernel": "poly"}),
    ("RandomForestClassifier criterion=gini", RandomForestClassifier, {"criterion": "gini"}),
    ("RandomForestClassifier criterion=entropy", RandomForestClassifier, {"criterion": "entropy"}),
    ("KneighborsClassifier n_neighbors=1", KNeighborsClassifier, {"n_neighbors":1})
]

models = []

for i in range(9):
    
    for modelname, Model, kwargs in model_metadata:
        
        model, score = train(xmm, y.loc[:, "increase"], Model, kwargs)

        print(i, modelname, " "*(50-len(modelname)), "accuracy score:", round(score,4), end="\r")

        models.append((modelname,model))

print()

import pickle

pickle.dump(models, open("scripts/generate_npl_forecasting_model/models/models.sav", "wb"))

print("trained models has been pickled and saved under scripts/generate_npl_forecasting_model/models/models.sav\n")