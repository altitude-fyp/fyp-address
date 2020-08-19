"""
    placehholder app as of now
"""

import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return flask.jsonify({"message": "hello from homepage"})

from app.api.exampleAPI import * 