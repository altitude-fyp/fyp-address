from components.common import *

def get_number_of_internet_hosts():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_hosts"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "number of internet hosts",
        "url": url,
        "desc": "number of internet hosts, based on 2012 figures by CIA Host Facebook",
        "data": read_table(table, ckey=0)
    }

def get_nummber_of_internet_users():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    custom_headers = [
        "number",
        "country",
        "internet users",
        "population",
        "population rank",
        "internet users percentage",
        "internet users percentage rank",
        "source"
    ]

    return {
        "name": "number of internet users",
        "url": url,
        "desc": "number of internet users (any person who has accessed the internet in the last 12 months using any device)",
        "data": read_table(table, custom_headers=custom_headers)
    }