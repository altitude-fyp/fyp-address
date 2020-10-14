# Generate NPL forecasting model

NOTE: this script is to be run from the backend directory
```
python generate_npl_forecasting_model/run.py
```

This script is divided into 3 sections

1. preprocessing
    - cleans aggregate.charts data
    - fills null values
    - saves as scripts/generate_npl_forecasting_model/npl.csv
    - saves data from latest year (no target variable) as scripts/generate_npl_forecasting_model/topredict.csv

2. train
    - trains a number of models using npl.csv
    - pickle saves them in scripts/generate_npl_forecasting_model/models/models.sav

3. predict
    - selects best model from trained models
    - uses model to predict topredict.csv

    output: {
        country_name: 0 if NPL is predicted to fall, 1 if NPL predicted to rise
    }

    - saved in pickled/npl_binary_forecasting.sav

run.py runs these 3 scripts in order

