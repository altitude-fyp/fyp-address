import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "hello world"}
    
"""
uvicorn main:app --reload to run server
"""