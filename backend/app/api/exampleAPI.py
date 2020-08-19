from app import *

@app.route("/api/example")
def exampleAPI_():
    return flask.jsonify({
        "message": "this is from example api"
    })