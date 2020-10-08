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
6. run automated test
```
pytest tests/run.py
```

## Running fastapi app 

Running for production
```
uvicorn app:app --workers 4
```

Running for development purposes
```
uvicorn app:app --reload
``` 
- the "--reload" argument reruns the entire app if there are any changes in code base

visit localhost:8000 to visit app
visit localhost:8000/docs to see swagger UI (auto-generated)

## Ubuntu help

1. finding pid of app running on port number
```
sudo lsof -t -i:<port number>
```
2. killing pid / killing app running on port
```
sudo kill <pid from step 1>
```

