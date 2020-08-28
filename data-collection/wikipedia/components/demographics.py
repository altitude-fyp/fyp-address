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
        "desc": "age structure by country (as of 2017)",
        "data": read_table(table, custom_headers=custom_headers)
    }

def get_homeless_population():
    """
    returns homeless population by country
    """

    url = "https://en.wikipedia.org/wiki/List_of_countries_by_homeless_population"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "homeless population by country",
        "data": read_table(table)
    }

def get_number_of_births():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_number_of_births"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "number of births by country (in thousands, as of year 2017)",
        "data": read_table(table)
    }

def get_national_capitals_by_population():
    url = "https://en.wikipedia.org/wiki/List_of_national_capitals_by_population"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "list of national capitals, ordered according to population",
        "data": read_table(table)
    }

def get_total_fertility_rate():
    url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependencies_by_total_fertility_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "total fertility rate ranked by country",
        "data": read_table(table)
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
        "desc": "Literacy rate by country",
        "data": read_table(table, custom_headers=custom_headers)
    }

def get_median_age():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_median_age"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "median age by country",
        "data": read_table(table)
    }

def get_labour_force_composition():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_sector_composition_of_the_labor_force"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "labour force compositions by country",
        "data": read_table(table)
    }

def get_sex_ratio():
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_sex_ratio'
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "sex ratio (male/female ratio) by country",
        "data": read_table(table)
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
        "desc": "tertiary education attainment by country",
        "data": read_table(table, custom_headers=custom_headers)
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
        "desc": "Traffic-related death rate by country - annual number of road fatalities per capita per year, per number of motor vehicles, and per vehicle-km",
        "data": read_table(table, custom_headers=custom_headers)
    }