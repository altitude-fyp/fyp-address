# Data aggregator
- this module is to be run after all data-collection scripts have been run

## For development/maintenance purposes
1. data-aggregator/pull.py
- this script pulls data from mongodb (which takes quite a while) and stores it using pickle in the data-aggregator/pickled folder
- don't worry as the pickled folder is gitignored
```
python data-aggregator/pull.py
```


2. data-aggregator/main.py
- this script does the data-processing and combination
- this script does not pull any data from mongodb, but reads pickled data from the data-aggregator/pickled folder
- this saves an average of 10 seconds every time you run main.py for development purposes
```
python data-aggregator/main.py
```

3. data-aggregator/run.py
- this script simply runs pull.py, then main.py
```
python data-aggregator/run.py
```

## Structure of aggregated data on mongodb
1. aggregate.countries
- this collection contains cleaned and combined data from dbpedia and wikipedia
- this collection is to be used with aggregate.charts for the frontend display

2. aggregate.charts
- this collection contains cleaned data only from imf (time-series data)
- this collection is to be used with aggregate.countries for the frontend display

3. aggregate.embeddings
- this collection contains cleaned data from dbpedia, wikipedia and imf
- this collection is meant to be as machine-readable as possible, and the values in the key-value pairs contained here are either numbers, string or null (no lists or dictionaries)
- for time series data, the latest value is taken as the main value