"""
    placehholder app as of now
"""

import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "hello world from the homepage"

if __name__ == "__main__":
    app.run()