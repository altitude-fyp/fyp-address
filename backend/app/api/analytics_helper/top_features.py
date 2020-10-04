from common import *
from mongodb_helper import *
import pandas as pd

raw = {}
for i in get_database()["test.aggregate.embeddings"].find():
    raw[i["_id"]] = i["data"]

# converting raw dictionary into pd dataframe object
data = pd.DataFrame(raw).T

t1 = "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Asset Quality, Non-performing Loans to Total Gross Loans, Percent"
t2 = "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Capital Adequacy, Non-performing Loans Net of Provisions to Capital, Percent"

# extracting x and y features + renaming target variables to t1 and t2
X = data.loc[:,[i for i in data.columns if i not in [t1, t2]]]
Y = data.loc[:,[t1,t2]]
Y.columns = ["t1", "t2"]

from sklearn.preprocessing import MinMaxScaler

# minmax scaler to transform all x values within range of 0 and 1
mmscaler = MinMaxScaler()
Xmm = mmscaler.fit_transform(X)

import math

# feature engineering on target variables
Y["t1_inverse"] = 1/Y["t1"]
Y["t2_inverse"] = 1/Y["t2"]
Y["t1_squared"] = Y["t1"] ** 2
Y["t2_squared"] = Y["t2"] ** 2
Y["t1_inverse_squared"] = 1/Y["t1"]**2
Y["t2_inverse_squared"] = 1/Y["t2"]**2
Y["t1_squareroot"] = Y["t1"] ** 0.5 # none for t2 cus t2 has negative values
Y["t1_log_e"] = [math.log1p(i) for i in Y["t1"]] # none for t2 cus t2 has negative values
Y["t1_exp"] = [math.exp(i) for i in Y["t1"]]
Y["t2_exp"] = [math.exp(i) for i in Y["t2"]]

# code to eliminate the printing of warnings
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

# training models here
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

models = {
    "linear regression": (LinearRegression, {}),
    "linear regression (normalize=True)": (LinearRegression, {"normalize": True}),

    "ridge": (Ridge, {}),
    "ridge (alpha=0.1)": (Ridge, {"alpha": 0.1}),
    "ridge (alpha=10)": (Ridge, {"alpha": 10}),

    "lasso": (Lasso, {}),
    "lasso (alpha=0.1)": (Lasso, {"alpha": 0.1}),
    "lasso (alpha=10)": (Lasso, {"alpha": 10}),

    "elastic net": (ElasticNet, {}),
    "elastic net (alpha=0.1)": (ElasticNet, {"alpha":0.1}),
    "elastic net (alpha=10)": (ElasticNet, {"alpha":10}),

    "SGDRegressor": (SGDRegressor, {}),
    "SGDRegressor (alpha=0.001)": (SGDRegressor, {"alpha":0.001}),
    "SGDRegressor (alpha=0.01)": (SGDRegressor, {"alpha":0.01}),
    "SGDRegressor (alpha=0.1)": (SGDRegressor, {"alpha":0.1}),
    "SGDRegressor (alpha=1)": (SGDRegressor, {"alpha":1}),
    "SGDRegressor (alpha=10)": (SGDRegressor, {"alpha":10}),
    
    "SVR (kernel=linear)": (svm.SVR, {"kernel": "linear"}),
    "SVR (kernel=linear, C=0.1)": (svm.SVR, {"kernel": "linear", "C":0.1}),
    "SVR (kernel=linear, C=10)": (svm.SVR, {"kernel": "linear", "C":10}),

    "LinearSVR": (svm.LinearSVR, {}),
    "LinearSVR (C=0.1)": (svm.LinearSVR, {"C":0.1}),
    "LinearSVR (C=10)": (svm.LinearSVR, {"C":10}),

    "NuSVR (kernel=linear)": (svm.NuSVR, {"kernel": "linear"}),
    "NuSVR (kernel=linear, C=0.1)": (svm.NuSVR, {"kernel": "linear", "C":0.1}),
    "NuSVR (kernel=linear, C=10)": (svm.NuSVR, {"kernel": "linear", "C":10}),
}

report = {}

NUM_ITER = 1000

for i in range(NUM_ITER):

    print("iteration", i+1, end="\r")
    
    for yname in Y:

        y = Y.loc[:,yname]
        xmm_train, xmm_test, y_train, y_test = train_test_split(Xmm, y)

        for modelname, (Model, kwargs) in models.items():

            model = Model(**kwargs)
            model.fit(xmm_train, y_train)

            y_pred = model.predict(xmm_test)
            score = r2_score(y_test, y_pred)

            if score < 0.2: model = None

            if (yname, modelname) not in report:
                report[(yname, modelname)] = [(model, score)]

            else:
                report[(yname, modelname)].append((model, score))

for k,v in report.items():
    v.sort(key=lambda x:x[-1])
    report[k] = v[len(v)//2]

report = [(yname, modelname, model, score) for (yname, modelname),(model,score) in report.items() if model]
report.sort(key=lambda x:-x[-1])

yname, modelname, model, score = report[0]

coefs = model.coef_
if len(coefs.shape) == 2:
    coefs = coefs[0]

assert len(coefs.shape) == 1

weights = [(xname, coef) for xname, coef in zip(X.columns, coefs)]
weights.sort(key=lambda x:x[-1])

import pickle

dump = yname, modelname, model, score, weights

pickle.dump(dump, open("analytics/models/top_features.sav", "wb"))

print("\ndone pickling")