# Generate country similarity matrix

NOTE: this script is to be run from the backend directory

```
python scripts/generate_country_similarity_matrix/run.py
```

This script:
1. pulls all embeddings data from aggregate.embeddings
2. computes cosine similarity for each country against every other country
3. saves as pickled/country_similarity_matrix.sav