import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}

@app.get("/")
async def example():
    return {"message": "this is an example!"}
