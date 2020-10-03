# Backend application for FYP address

## Environment Set-up
1. create .env file
2. Create virtual python environment
```
python3 -m venv env
```
3. Activate venv
```
source env/bin/activate
``` 
4. install dependencies on venv
```
pip3 install -r requirements.txt
```
5. run scripts/run.py
```
python3 scripts/run.py
```

## Running fastapi app 
```
uvicorn app:app --reload
```

visit localhost:8000 to visit app
visit localhost:8000/docs to see swagger UI (auto-generated)

## API

1. Get all countries
```
/api/countries
```
Returns country-level data for all countries 

2. Get country
```
/api/countries/{country_name}
```
Returns country-level data for 1 country

3. Get all regions in country
```
/api/regions/{country_name}
```
Returns region-level data for all regions in 1 country

4. Get Region
```
/api/regions/{country_name}/{region_name}
```
Returns region-level data for 1 region in 1 country

5. TBC