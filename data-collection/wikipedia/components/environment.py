from components.common import *

def get_co2_emissions():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita"
    soup = get_soup(url)

    def edit_headers(headers):
        headers[0] = "country"

    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "",
        "data": read_table(table, edit_headers=edit_headers)
    }

def get_natural_gas_consumption():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_consumption"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "natural gas consumption bby country",
        "data": read_table(table)    
    }