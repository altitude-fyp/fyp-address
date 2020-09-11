import fastapi

app = fastapi.FastAPI()

@app.get("/")
def root():
    return {"message": "This is the backend for address-fyp"}

from app.api.countries import *
from app.api.regions import *
from app.api.email_notifications import *
