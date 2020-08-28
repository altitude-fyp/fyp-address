from components.common import *

def get_bmi():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_body_mass_index"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "bmi",
        "url": url,
        "desc": "body mass index by country (as of 2015)",
        "data": read_table(table, ckey=0)
    }

def get_HIV_AIDS_prevalence():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_HIV/AIDS_adult_prevalence_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "HIV and AIDS prevalence",
        "url": url,
        "desc": "HIV/AIDS prevalence estimates by country",
        "data": read_table(table, ckey=0)
    }

def get_infant_and_under_five_mortality_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_infant_and_under-five_mortality_rates"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable", "id": "worldbank"})

    return {
        "name": "infant mortality rate",
        "url": url,
        "desc": "mortality rate of infants/children under 5 per 1000 live births (as of 2018)",
        "data": read_table(table, ckey=0)
    }

def get_life_expectancy():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    custom_headers = [
        "rank",
        "country",
        "overall",
        "female",
        "male"
    ]

    return {
        "name": "life expectancy",
        "url": url,
        "desc": "life expectancy (as of 2018)",
        "data": read_table(table, custom_headers=custom_headers)
    }

def get_maternal_mortality_ratio():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_maternal_mortality_ratio"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    # unable to use read_table due to weird data format
    data = []
    headers = ["country", "maternal mortality ratio per 100,000 live births"]

    for tr in table.find_all("tr"):
        try:
            tds = tr.find_all("td")
            assert len(tds) >= 2

            *_, country, rate = [td.text.strip() for td in tds]

            data.append({
                "country": country,
                "maternal mortality ratio per 100,000 live births": rate
            })

        except:pass

    return {
        "name": "maternal mortality rate",
        "url": url,
        "desc": "maternal mortality rate (per 100,000 live births) by country - the death of a woman while pregnant or within 42 days of termination of pregnancy, irrespective of the duration and site of the pregnancy, from any cause related to or aggravated by the pregnancy or its management but not from accidental or incidental causes",
        "data": data
    }

def get_mortality_rate():
    url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_mortality_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    data = []
    for tr in table.find_all("tr"):
        try:
            tds = tr.find_all("td")
            assert len(tds) == 5
            tds = [td.text.strip() for td in tds]

            country, *_, rate, __ = tds
            data.append({
                "country": country,
                "mortality rate per 1000": rate
            })

        except:pass

    return {
        "name": "mortality rate",
        "url": url,
        "desc": "mortality rate per 1000 people (as of 2017)",
        "data": data
    }

def get_number_of_physicians():
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_number_of_physicians"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    custom_headers = ["country", "size (2000-2009)", "physicians per 1000 people (2000-2009)", "physicians per 1000 people (2007-2013)"]

    return {
        "name": "number of physicians",
        "url": url,
        "desc": "number of physicians per 1000 people by country",
        "data": read_table(table, custom_headers=custom_headers)
    }

def get_proportion_of_population_using_improved_sanitation_facilities():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_proportion_of_the_population_using_improved_sanitation_facilities"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "population using improved sanitation",
        "url": url,
        "desc": """proportion of population using improved sanitation facilities -
                        Flush toilet
                        Connection to a piped sewer system
                        Connection to a septic system
                        Flush / pour-flush to a pit latrine
                        Ventilated improved pit (VIP) latrine
                        Pit latrine with slab
                        Composting toilet
                    """,

        "data": read_table(table, ckey=0)
    }

def get_cigarette_consumption_per_capita():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_cigarette_consumption_per_capita"
    soup = get_soup(url)
    table = soup.find("table", {"class": "sortable"})

    return {
        "name": "cigarette consumption",
        "url": url,
        "desc": "cigarette consumption per year per capita (persons aged >= 15)",
        "data": read_table(table, ckey=1)
    }