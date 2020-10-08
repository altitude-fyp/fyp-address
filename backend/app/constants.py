"""
this file contains all constants used in the application

    - all_countries is a dictionary
    
        key = country name
        value = {
            lat: latitude,
            lon :longitude,
            code: 2 letter country code,
            flag: link to country flag
        }
"""

import pickle

COUNTRIES = pickle.load(open("pickled/all_countries.sav", "rb"))


COUNTRY_FEATURE_CATEGORIES = [
        {
            "category": "Economic Information",
            "value": [
                "Gdp nominal",
                "Gdp nominal per capita",
                "Gdp ppp",
                "Gdp ppp per capita",
                "Gini",
                "Hdi",
                "GNI per capita (female)",
                "GNI per capita (male)",
                "Male to female income ratio",
                "Government budget per capita",
                "Oil imports",
                "Net oil exports",
                "Foreign exchange reserves (million USD)",
                "Tariff rate",
                "Unemployment rate",
                "Consumer Price Index, All items",
                "Geographical Outreach, Number of Institutions, Other deposit takers",
                "Geographical Outreach, Number of Institutions, Insurance corporations",
                "Use of Financial Services, Number of Borrowers, Commercial banks",
                "Key Indicators, Use of Financial Services, Outstanding loans from commercial banks (% of GDP)",
                "Geographical Outreach, Number of Branches, Excluding Headquarters, Commercial banks",
                "Financial Development Index",
                "Financial Institutions Access Index",
                "Financial Institutions Efficiency Index",
                "Financial Institutions Index",
                "Financial Markets Access Index",
                "Financial Markets Depth Index",
                "Financial Markets Efficiency Index",
                "Financial Markets Index",
                "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Asset Quality, Non-performing Loans to Total Gross Loans, Percent",
                "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Capital Adequacy, Non-performing Loans Net of Provisions to Capital, Percent",
                "Use of Financial Services, Number of Loan Accounts, Commercial banks"
            ]
        },
        {
            "category": "Population Information",
            "value": [
                "Population density",
                "Population total",
                "Age structure (0-14 years)",
                "Age structure (15-64 years)",
                "Age structure (over 65 years)",
                "Number of births (in thousands)",
                "Capital population",
                "Fertility rate",
                "Literacy rate",
                "Male literacy rate",
                "Female literacy rate",
                "Median age",
                "Median male age",
                "Median female age",
                "Labour force",
                "Labour force (agriculture)",
                "Labour force (industry)",
                "Labour force (service)",
                "Sex ratio (at birth)",
                "Sex ratio (0-14 years)",
                "Sex ratio (15-24 years)",
                "Sex ratio (25-54 years)",
                "Sex ratio (55-64 years)",
                "Sex ratio (over 65 years)",
                "Sex ratio (total)",
                "Financial Institutions Depth Index",
                "Oil production",
                "Geographical Outreach, Number of Institutions, Credit unions and credit cooperatives"
            ]
        },
        {
            "category": "Mortality Information",
            "value": [
                "Intentional homicide rate",
                "Intentional homicide rate count",
                "Cocaine use",
                "Total firearm death rate",
                "Firearm death rate by homicide",
                "Firearm death rate by suicide",
                "Unintentional firearm death rate",
                "Undetermined firearm death rate",
                "Guns per 100 inhabitants",
                "Opiate use",
                "Suicide rate",
                "Male suicide rate",
                "Female suicide rate",
                "Suicide rate (male:female ratio)",
                "Suicide rate rank",
                "Traffic-related death rate (per 100,000 inhabitants per year)",
                "Traffic-related death rate (per 100,000 motor vehicles)",
                "Traffic-related death rate (total)",
                "Dependency ratio (total)",
                "Dependency ratio (youth)",
                "Dependency ratio (elderly)",
                "Potential support ratio",
                "Infant mortality rate under 5 (per 1000 lives births)",
                "Life expectancy (overall)",
                "Life expectancy (female)",
                "Life expectancy (male)",
                "Maternal mortality rate (per 100,000 live births)",
                "Mortality rate (per 1000 people)"
            ]
        },
        {
            "category": "Other Information",
            "value": [
                "Cocaine use",
                "Co2 emissions (tonnes)",
                "Natural gas consumption (million m3 per year)",
                "Overall mean BMI",
                "Female mean BMI",
                "Male mean BMI",
                "Number of physicians (per 1000 people)",
                "Proportion of population using improved sanitation",
                "Cigarette consumption (per year per capita)",
                "Number of internet hosts",
                "Number of internet users",
                "Homeless population per night",
                "Number of people with HIV/AIDS",
                "Homeless population per 10000 people",
                "HIV/AIDS prevalence (adults)"
            ]
        },
    ]