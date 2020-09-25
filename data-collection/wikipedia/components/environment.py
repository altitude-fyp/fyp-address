from components.common import *

def get_co2_emissions():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions_per_capita"
    soup = get_soup(url)

    def edit_headers(headers):
        headers[0] = "country"

    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "co2 emissions (tonnes)",
        "url": url,
        "desc": "co2 emissions per capita by country (in tons)",
        "data": read_table(table, edit_headers=edit_headers),
        "main": "2018"
    }

def get_natural_gas_consumption():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_natural_gas_consumption"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    headers = ["rank", "country", "consumption (million m3 per year)", "date of info"]

    return {
        "name": "natural gas consumption (million m3 per year)",
        "url": url,
        "desc": "natural gas consumption by country",
        "data": read_table(table, ckey=1, custom_headers=headers),
        "main": "consumption (million m3 per year)"
    }