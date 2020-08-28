import requests
from bs4 import BeautifulSoup

def get_countries_and_cities():
    wiki, wiki_errors = get_wikipedia_countries_and_cities()
    citi = get_citibank_countries()

    return sorted([(k,v) for k,v in wiki.items() if k in citi], key=lambda x:x[0])


def get_citibank_countries():
    """
    reads list of countries citibank operates in (from citi website)
    returns set of countries
    """
    with open("dbpedia/citibank_countries.txt") as f:
        return set([line.strip() for line in f])

def get_wikipedia_countries_and_cities():
    
    """
    returns large dictionary of countries and cities inside countries
    """

    BASE_URL = "https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_"

    out = {}
    errors = []

    for letter in "abcdefghijklmnopqrstuvwxyz".upper():
        url = BASE_URL + letter
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        table = soup.find("table")
        for tr in table.find_all("tr"):
            try:
                tds = tr.find_all("td")
                assert len(tds) == 2

                city, country = tds
                city = city.text.strip()
                country = country.text.strip()

                if country not in out: out[country] = []
                
                out[country].append(city)

            except Exception as err:
                errors.append(
                    {"url": url, "error": str(err)}
                )

    """
    arrange out by alphabetical order
    """
        
    return out, errors




def parse_dbpedia_page(url):
    """
        scrapes dbpedia page given in url
        returns dictionary representing dbpedia article object
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    table = soup.find("table", {"class": "description"})
    out = {}

    for tr in table.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) == 2:
            k,v = tds
            k = k.find("a").text.strip()

            value = []
            for li in v.find("ul").find_all("li"):
    
                item = None
                try:
                    a = li.find("a")
                    item = {
                        "href": a["href"],
                        "name": a.text.strip()
                    }
                except:
                    item = li.text.strip()

                value.append(item)

            value = value[0] if len(value)==1 else value

            out[k] = value
        
    return out

DBPEDIA_BASE = "http://dbpedia.org/page/"
