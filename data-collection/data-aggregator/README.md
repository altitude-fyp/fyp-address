# Data aggregator
- this module is to be run after all data-collection scripts have been run

## For developers
1. Run pull.py first to pull all raw data sources and store them using pickle
    - create a pickled folder under the data-collection directory
    - all raw data will be stored isnide the pickled folder so we dont need to wait 25 seconds everytime we pull data from mongodb
    - don't worry as the pickled folder is gitignored
```
python data-aggregator/run.py
```

2. You can now work on and run main.py, which pulls data from the pickled folder
    - main.py does not touch mongodb at all - it interacts only with the pickled folder

3. Data is combined in 2 ways - combine as embeddings and combine as api data

### Combine as embeddings
- purpose: make data machine readable
- every value in each country object is either a float, string or null value
- no nested list/dict data structures for machine readability 
- stored in embeddings.countries collection on mongodb

### Combine as api data
- purpose: make data human readable for frontend use
- more nested data structures and descriptions about data
- stored in aggregate.countries collection on mongodb