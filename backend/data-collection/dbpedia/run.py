import requests
from helper import extract_urls

"""

data to be saved:

1. Singapore.json
2. JSON representation of every unique link in singapore.json

Format data is saved (MongoDB)
    - link as key
    - JSON representation as value
"""

SINGAPORE_URL = "http://dbpedia.org/data/Singapore.json"
r = requests.get(SINGAPORE_URL)
singapore = r.json()

out = {SINGAPORE_URL: singapore}

urls = extract_urls(singapore)
for url in urls:
    try:
        """
            placeholder 
        """
        print(url)

    except Exception as err:
        print(str(err))


