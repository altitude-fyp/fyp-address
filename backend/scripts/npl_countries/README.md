# Retrieve NPL data

NOTE: this script is to be run from the backend directory

```
python scripts/npl_countries/run.py
```

This script:
1. generates a pickle file containing all non-performing loans used frequently by the backend
2. function to return country specific non-performing loans for visualisation 
3. saves as /backend/pickled/all_npl_data.sav