from components.common import *

def get_intentional_homicide_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate"
    soup = get_soup(url)
    table = soup.find("table", {"id": "UNODC"})

    return {
        "desc": "number of intentional homicide victims per 100,000 inhabitants",
        "data": read_table(table)
    }

def get_prevalence_of_cocaine_use():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_prevalence_of_cocaine_use"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "prevalence of cocaine use: percentage of adults and youths who have consumed the drug at least once in the past year",
        "data": read_table(table)
    }

def get_firearm_death_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_firearm-related_death_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "firearm death rate per 100,000 population per year by country",
        "data": read_table(table)
    }

def get_prevalence_of_opiates_use():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_prevalence_of_opiates_use"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "desc": "annual prevalence of opiates use by country",
        "data": read_table(table)
    }

def get_suicide_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate"
    soup = get_soup(url)
    table = soup.find_all("table", {"class": "sortable"})[2]

    return {
        "desc": "suicide rate (per 100,000 people) by country",
        "data": read_table(table)
    }

def get_terrorist_incidents():
    url = "https://en.wikipedia.org/wiki/Number_of_terrorist_incidents_by_country"
    soup = get_soup(url)
    table = soup.find_all("table", {"class": "wikitable"})[1]

    return {
        "desc": "number of terrorist incidents by country",
        "data": read_table(table)
    }