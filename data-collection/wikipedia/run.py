"""
Taken from https://en.wikipedia.org/wiki/Category:Lists_of_countries
"""

from components.crime import *
from components.economics import *
from components.environment import *
from components.health import *
from components.demographics import *
from components.technology import *

print("scraping crime data")

crime = [
    get_intentional_homicide_rate(),
    get_prevalence_of_cocaine_use(),
    get_firearm_death_rate(),
    get_prevalence_of_opiates_use(),
    get_suicide_rate(),
    get_terrorist_incidents()
]

print("done scraping crime data\n")
print("scraping demographics data")

demographics = [
    get_age_structure(),
    get_homeless_population(),
    get_number_of_births(),
    get_national_capitals_by_population(),
    get_total_fertility_rate(),
    get_literacy_rate(),
    get_median_age(),
    get_labour_force_composition(),
    get_sex_ratio(),
    get_tertiary_education_attainment(),
    get_traffic_related_death_rate()
]

print("done scraping demographics data\n")
print("scraping economics data")

economics = [
    get_dependency_ratio(),
    get_male_female_income_ratio(),
    get_government_budget_per_capita(),
    get_oil_exports(),
    get_oil_imports(),
    get_net_oil_exports(),
    get_oil_production(),
    get_foreign_exchange_reserves(),
    get_tariff_rate(),
    get_unemployment_rate()
]

print("done scraping economics data\n")
print("scraping environment data")

environment = [
    get_co2_emissions(),
    get_natural_gas_consumption()
]

print("done scraping environment data\n")
print("scraping health data")

health = [
    get_bmi(),
    get_HIV_AIDS_prevalence(),
    get_infant_and_under_five_mortality_rate(),
    get_life_expectancy(),
    get_maternal_mortality_ratio(),
    get_mortality_rate(),
    get_number_of_physicians(),
    get_proportion_of_population_using_improved_sanitation_facilities(),
    get_cigarette_consumption_per_capita()
]

print("done scraping health data\n")
print("scraping technology data")

technology = [
    get_number_of_internet_hosts(),
    get_nummber_of_internet_users()    

]

print("done scraping technology data\n")

data = crime + demographics + economics + environment + health + technology

import sys
here = sys.path[0]
sys.path.append(here[:-len("wikipedia")])

from mongodb_helper import *

mongo_upsert(
    data={
            "_id": "wiki",
            "data": data
        },
    collection_name="wikipedia",
    replacement_pattern={"_id": "wiki"}
)