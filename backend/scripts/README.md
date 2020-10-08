# IMPORTANT!!! TO MY FELLOW DEVELOPERS:

1. the scripts folder is for scripts (duh) that are supposed to be run once
2. these scripts take a very very long time to run and hence will not be part of our fastapi api
3. instead, these scripts are to be run right after data collection together with the batch job
4. these scripts will train models / perform calculations / whatever and SAVE IT USING PICKLE in a .sav file
5. the api will READ FROM THE PICKLED FILES cus its much faster
6. the pickled files will be stored under scripts/pickled
7. DO NOT REMOVE THIS FOLDER

## Running the scripts here
1. The run.py will run everything
2. run this from the backend directory

```
python scripts/run.py
```