# Backend application for FYP address

## Environment set-up
```
cd backend

(Create a python virtual environment)
python3 -m venv env (for MacOS)
python -m venv env (for windows)

(Activate your python virtual environment)
source env/bin/activate

(Install python dependencies needed by the app)
pip3 install -r requirements.txt

```

## Running fastapi app 
```
uvicorn main:app --reload
```

visit localhost:8000 to visit app
visit localhost:8000/docs to see swagger UI (auto-generated)