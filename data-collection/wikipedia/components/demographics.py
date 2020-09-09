from components.common import *

def get_age_structure():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_age_structure"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    custom_headers = [
        "country",
        "age 0-14 years",
        "age 15-64 years",
        "age over 65 years"
    ]
    return {
        "name": "age structure",
        "url": url,
        "desc": "age structure by country (as of 2017)",
        "data": read_table(table, custom_headers=custom_headers),
        "main": ["age 0-14 years", "age 15-64 years", "age over 65 years"]
    }

def get_homeless_population():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_homeless_population"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    custom_headers = ["country", "homeless population per night", "data year", "homeless per 10000", "notes"]

    return {
        "name": "homeless population",
        "url": url,
        "desc": "homeless population by country",
        "data": read_table(table, ckey=0, custom_headers=custom_headers),
        "main": ["homeless population per night", "homeless per 10000"]
    }

def get_number_of_births():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_number_of_births"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    custom_headers = ["rank", "country", "number of births in thousands"]

    return {
        "name": "number of births",
        "url": url,
        "desc": "number of births by country (in thousands, as of year 2017)",
        "data": read_table(table, ckey=1, custom_headers=custom_headers),
        "main": "number of births in thousands"
    }

def get_national_capitals_by_population():
    url = "https://en.wikipedia.org/wiki/List_of_national_capitals_by_population"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "capital population",
        "url": url,
        "desc": "list of national capitals, ordered according to population",
        "data": read_table(table, ckey=1),
        "main": "Population"
    }

def get_total_fertility_rate():
    url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependencies_by_total_fertility_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    headers = ["rank", "country", "fertility rate"]

    return {
        "name": "fertility rate",
        "url": url,
        "desc": "total fertility rate ranked by country",
        "data": read_table(table, ckey=1, custom_headers=headers),
        "main": "fertility rate"
    }

def get_literacy_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_literacy_rate"
    soup = get_soup(url)
    table = soup.find_all("table", {"class": "sortable"})[1]

    custom_headers = [
        "country",
        "literacy rate (all)",
        "male literacy",
        "female literacy",
        "gender difference",
        "non-UNESCO literacy rate"
    ]

    return {
        "name": "literacy rate",
        "url": url,
        "desc": "Literacy rate by country",
        "data": read_table(table, custom_headers=custom_headers),
        "main": ["literacy rate (all)", "male literacy", "female literacy", "gender difference"]
    }

def get_median_age():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_median_age"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "median age",
        "url": url,
        "desc": "median age by country",
        "data": read_table(table, ckey=0),
        "main": ["Median(Years)", "Male(Years)", "Female (Years)"]
    }

def get_labour_force_composition():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_sector_composition_of_the_labor_force"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "labour force composition",
        "url": url,
        "desc": "labour force compositions by country",
        "data": read_table(table, ckey=1),
        "main": ["Labour force", "Agriculture", "Industry", "Service"]
    }

def get_sex_ratio():
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_sex_ratio'
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    headers = ["country", "at birth", "0 to 14 years", "15 to 24 years", "25 to 54 years", "55 to 64 years", "over 65", "total"]

    return {
        "name": "sex ratio",
        "url": url,
        "desc": "sex ratio (male/female ratio) by country",
        "data": read_table(table, ckey=0, custom_headers=headers),
        "main": ["at birth", "0 to 14 years", "15 to 24 years", "25 to 54 years", "55 to 64 years", "over 65", "total"]
    }

def get_tertiary_education_attainment():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_tertiary_education_attainment"
    soup = get_soup(url)
    table = soup.find_all("table", {"class": "wikitable"})[1]

    custom_headers = [
        "country",
        "equivalent to 2 year degree or higher (%)",
        "equivalent to 4 year degree or higher (%)",
        "equivalent to 6 year degree or higher (%)",
        "year",
        "non-OECD"
    ]

    return {
        "name": "tertiary education",
        "url": url,
        "desc": "tertiary education attainment by country",
        "data": read_table(table, custom_headers=custom_headers),
        "main": [   
            "equivalent to 2 year degree or higher (%)",
            "equivalent to 4 year degree or higher (%)",
            "equivalent to 6 year degree or higher (%)"
        ]
    }

def get_traffic_related_death_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_traffic-related_death_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    custom_headers = [
        "country",
        "continent",
        "road fatalities per 100,000 inhabitants per year",
        "road fatalities per 100,000 motor vehicles",
        "road fatalities per 1 billion vehicle-km",
        "total fatalities in latest year",
        "year"
    ]

    return {
        "name": "traffic-related death rate",
        "url": url,
        "desc": "Traffic-related death rate by country - annual number of road fatalities per capita per year, per number of motor vehicles, and per vehicle-km",
        "data": read_table(table, custom_headers=custom_headers),
        "main": [
            "road fatalities per 100,000 inhabitants per year",
            "road fatalities per 100,000 motor vehicles",
            "road fatalities per 1 billion vehicle-km",
            "total fatalities in latest year"
        ]
    }