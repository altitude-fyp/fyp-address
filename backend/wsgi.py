"""
gunicorn --bind 0.0.0.0:5000 --workers=4 wsgi:app

to run using gunicorn
"""

from app import *

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")