from app import app

@app.get("/example/{number}")
def example(number: int):
    return {
        "message": "this is an example!",
        "number": number
    }