from components.common import *

def get_dependency_ratio():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_dependency_ratio"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    custom_headers = [
        "country",
        "total dependency ratio",
        "youth dependency ratio",
        "elderly dependency ratio",
        "potentail support ratio"
    ]

    return {
        "name": "dependency ratio",
        "url": url,
        "desc":"""returns dependency ratio by country - economically/financially dependent on working class 
    total dependency ratio - The total dependency ratio is the ratio of combined youth population (ages 0-14) and elderly population (ages 65+) per 100 people of working age (ages 15-64). A high total dependency ratio indicates that the working-age population and the overall economy face a greater burden to support and provide social services for youth and elderly persons, who are often economically dependent.
    youth dependency ratio - The youth dependency ratio is the ratio of the youth population (ages 0-14) per 100 people of working age (ages 15-64). A high youth dependency ratio indicates that a greater investment needs to be made in schooling and other services for children.
    elderly dependency ratio - The elderly dependency ratio is the ratio of the elderly population (ages 65+) per 100 people of working age (ages 15-64). Increases in the elderly dependency ratio put added pressure on governments to fund pensions and healthcare.
    potential support ratio - The potential support ratio is the number of working-age people (ages 15-64) per one elderly person (ages 65+). As a population ages, the potential support ratio tends to fall, meaning there are fewer potential workers to support the elderly.""",
        
        "data": read_table(table, custom_headers=custom_headers)
    }

def get_male_female_income_ratio():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_male_to_female_income_ratio"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "male female income ratio",
        "url": url,
        "desc": "male to female income ratio by country (as of 2017)",
        "data": read_table(table, ckey=0)
    }


def get_government_budget_per_capita():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_government_budget_per_capita"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "government budget per capita",
        "url": url,
        "desc": "total government budget (in USD) divided by total population (as of 2018)",
        "data": read_table(table, ckey=0)
    }

def get_oil_exports():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_exports"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "oil exports",
        "url": url,
        "desc": "oil exports by country",
        "data": read_table(table, ckey=1)
    }

def get_oil_imports():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_imports"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "oil imports",
        "url": url,
        "desc": "oil imports by country",
        "data": read_table(table, ckey=1)
    }

def get_net_oil_exports():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_net_oil_exports"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "net oil exports",
        "url": url,
        "desc": "net oil exports (oil exports - oil imports) by country",
        "data": read_table(table, ckey=1)
    }

def get_oil_production():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_oil_production"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    def edit_headers(headers):
        headers[0] = "number"

    return {
        "name": "oil production",
        "url": url,
        "desc": "oil production by country",
        "data": read_table(table, edit_headers=edit_headers, ckey=1)
    }

def get_foreign_exchange_reserves():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_foreign-exchange_reserves"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "foreign exchange reserves",
        "url": url,
        "desc": "foreign exchange reserves by country - the foreign-currency deposits held by national central banks and monetary authorities (See List of countries by foreign-exchange reserves (excluding gold)). However, in popular usage and in the list below, it also includes gold reserves, special drawing rights (SDRs) and International Monetary Fund (IMF) reserve position because this total figure, which is usually more accurately termed as official reserves or international reserves or official international reserves",
        "data": read_table(table, ckey=1)
    }

def get_tariff_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_tariff_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    data = []
    for tr in table.find_all("tr"):
        try:
            tds = tr.find_all("td")
            assert len(tds) >= 3
            *_, country, tariff, year = [td.text.strip() for td in tds]

            data.append({
                "country": country,
                "tariff rate": tariff,
                "year": year
            })

        except:pass

    return {
        "name": "tariff rate",
        "url": url,
        "desc": "tariff rate by country - import duty refers to taxes levied on imported goods, capital and services",
        "data": data
    }

def get_unemployment_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_unemployment_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "unemployment rate",
        "url": url,
        "desc": "unempployment rate by country",
        "data": read_table(table, ckey=0)
    }