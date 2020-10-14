"""
combines all models in models.sav into 1 general model

    for predictions, majority wins

    if more models predict an entry as 1, the final value will be 1

"""

import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

class AggregateModel():

    def __init__(self):
        self.models = pickle.load(open("scripts/generate_npl_forecasting_model/models/models.sav", "rb"))

    def predict(self, x):
        
        preds = []

        for modelname, model in self.models:
            
            pred = model.predict(x)
            preds.append([i for i in pred])
            
        out = []

        for i in range(len(preds[0])):
            
            country_preds = []

            for pred in preds:

                country_preds.append(pred[i])

            majority = 0
            if country_preds.count(0) < country_preds.count(1):
                majority = 1
            
            out.append(majority)

        return out

    def test(self):
        """
        testing aggregate model on training data
        """

        data = pd.read_csv("scripts/generate_npl_forecasting_model/npl.csv", sep="\t")

        y = data.iloc[:,:2]
        x = data.iloc[:,2:]

        # creating variable "increase" - whether next years's NPL is higher than current year
        y["increase"] = [1 if j>i else 0 for i,j in zip(y["npl"], y["npl_next"])]

        mmscaler = MinMaxScaler()
        mmscaler.fit(x)
        xmm = mmscaler.transform(x)

        y_pred = self.predict(xmm)

        print("accuracy score of aggregateModel:", accuracy_score(y_pred, y.loc[:,"increase"]), "\n")

        # print("\ntesting individual models\n")
        # for modelname, model in self.models:

        #     score = model.score(xmm, y.loc[:,"increase"])

        #     y_pred = model.predict(xmm)
        #     score2 = accuracy_score(y_pred, y.loc[:, "increase"])

        #     print(round(score,4), round(score2, 4), modelname)

