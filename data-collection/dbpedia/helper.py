import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_countries():
    """
    returns list of all countries
    """
    return list(pd.read_csv("dbpedia/countries.csv", delimiter="\t").loc[:,"Name"].values)


def scrape(url):
    """
    input: url of dbpedia page
    output: returns cleaned dictionary representing data in dbpedia page
    """

    useful_fields = set([
        'dbp:gdpNominal', 
        'dbp:gdpNominalPerCapita', 
        'dbp:gdpPpp', 
        'dbp:gdpPppPerCapita', 
        'dbp:hdi', 
        'dbo:populationDensity',  
        'dbp:gini', 
        'dbo:populationTotal', 
    ])

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    table = soup.find("table", {"class": "description"})

    out = {}
    for tr in table.find_all("tr"):
        
        tds = tr.find_all("td")

        if len(tds) != 2:
            continue

        k, v = tds
        k = k.find("a").text.strip()

        if k not in useful_fields:
            continue

        v = v.find("ul").find("li").text.strip()

        out[k] = v
    
    return out


DBPEDIA_BASE = "http://dbpedia.org/page/"
