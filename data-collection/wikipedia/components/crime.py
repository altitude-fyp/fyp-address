from components.common import *

def get_intentional_homicide_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate"
    soup = get_soup(url)
    table = soup.find_all("table", {"class": "wikitable"})[2]

    data = []
    headers = ["country", "region", "subregion", "rate", "count", "year"]
    for tr in table.find_all("tr"):

        try:
            country = tr.find("th").text.strip()
            tds = tr.find_all("td")
            assert len(tds) == 5
            region, subregion, rate, count, year = [td.text.strip() for td in tds]

            data.append({
                "country": country, 
                "region": region,
                "subregion": subregion,
                "rate": rate,
                "count": count,
                "year": year
            })

        except: pass

    return {
        "name": "intentional homicide rate",
        "url": url,
        "desc": "number of intentional homicide victims per 100,000 inhabitants",
        "data": data,
    }

def get_prevalence_of_cocaine_use():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_prevalence_of_cocaine_use"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "cocaine use",
        "url": url,
        "desc": "prevalence of cocaine use: percentage of adults and youths who have consumed the drug at least once in the past year",
        "data": read_table(table, ckey=0),
    }

def get_firearm_death_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_firearm-related_death_rate"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "firearm death rate",
        "url": url,
        "desc": "firearm death rate per 100,000 population per year by country",
        "data": read_table(table, ckey=0)
    }

def get_prevalence_of_opiates_use():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_prevalence_of_opiates_use"
    soup = get_soup(url)
    table = soup.find("table", {"class": "wikitable"})

    return {
        "name": "opiate use",
        "url": url,
        "desc": "annual prevalence of opiates use by country",
        "data": read_table(table, ckey=1)
    }

def get_suicide_rate():
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_suicide_rate"
    soup = get_soup(url)
    table = soup.find_all("table", {"class": "sortable"})[2]

    return {
        "name": "suicide rate",
        "url": url,
        "desc": "suicide rate (per 100,000 people) by country",
        "data": read_table(table, ckey=1)
    }

def get_terrorist_incidents():
    url = "https://en.wikipedia.org/wiki/Number_of_terrorist_incidents_by_country"
    soup = get_soup(url)
    table = soup.find_all("table", {"class": "wikitable"})[1]

    return {
        "name": "terrorist incident count",
        "url": url,
        "desc": "number of terrorist incidents by country",
        "data": read_table(table, ckey=0)
    }