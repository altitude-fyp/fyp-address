from app import app
from mongodb_helper import *

@app.get("/api/countries")
def get_countries_list():
  
    db = get_database()
    constant_collection = db["constant"]
    data = constant_collection.find_one({"_id": "continents"})

    out = {"status": "error", "data": None}
    if data:
        out["status"] = "success"
        out["data"] = data
    return out

def format_countries_filter(data_dict):
    data_list = []
    for key, value in data_dict.items():
        data_list.append(key)
    return data_list


@app.get("/api/countries/{country_name}")
def get_countries_data(country_name: str):

    db = get_database()
    aggregate_countries_collection = db["aggregate.embeddings"]

    out = {"status": "error", "data": {}}
    data = aggregate_countries_collection.find_one({"_id": country_name})

    if data:
        result = format_countries_data(data["data"])
        out["status"] = "success"
        out["data"]["filter"] = get_filter_list()
        out["data"]["top8"] = result[1]
        out["data"]["items"] = result[0]
    return out


def format_countries_data(data_dict):
    data_list = []
    top8_list = []
    top8_filter = ["Gdp nominal", "Hdi", "Financial Development Index", "Consumer Price Index, All items",
                   "Population total", "Area total", "Unemployment rate", "Life expectancy (overall)"]

    for key, value in data_dict.items():
        obj = {}
        obj["name"] = key
        obj["value"] = value
        data_list.append(obj)

        if key in top8_filter:
            top8_list.append(obj)

    return [data_list, top8_list]


def get_filter_list():
    return [
        {
            "category": "Economic Information",
            "value": [
                "Gdp nominal",
                "Gdp nominal per capita",
                "Gdp nominal rank",
                "Gdp nominal year",
                "Gdp ppp",
                "Gdp ppp per capita",
                "Gdp ppp per capita rank",
                "Gdp ppp year",
                "Gini",
                "Gini year",
                "Hdi",
                "Hdi rank",
                "Hdi year",
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
                "Population density rank",
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
                "Gdp nominal per capita rank",
                "Financial Institutions Depth Index",
                "Oil production",
                "Gdp ppp rank",
                "Geographical Outreach, Number of Institutions, Credit unions and credit cooperatives"
            ]
        },
        {
            "category": "Location Information",
            "value": [
                "Area total",
                "Area rank"

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

    def get_countries_latlong():
        return [{'name': 'United Arab Emirates', 'coordinates': {'lat': 23.424076, 'long': 53.847818}}, {'name': 'Argentina', 'coordinates': {'lat': -38.416097, 'long': -63.616672}}, {'name': 'Austria', 'coordinates': {'lat': 47.516231, 'long': 14.550072}}, {'name': 'Australia', 'coordinates': {'lat': -25.274398, 'long': 133.775136}}, {'name': 'Barbados', 'coordinates': {'lat': 13.193887, 'long': -59.543198}}, {'name': 'Bangladesh', 'coordinates': {'lat': 23.684994, 'long': 90.356331}}, {'name': 'Belgium', 'coordinates': {'lat': 50.503887, 'long': 4.469936}}, {'name': 'Bulgaria', 'coordinates': {'lat': 42.733883, 'long': 25.48583}}, {'name': 'Bahrain', 'coordinates': {'lat': 25.930414, 'long': 50.637772}}, {'name': 'Brazil', 'coordinates': {'lat': -14.235004, 'long': -51.92528}}, {'name': 'Bahamas', 'coordinates': {'lat': 25.03428, 'long': -77.39628}}, {'name': 'Canada', 'coordinates': {'lat': 56.130366, 'long': -106.346771}}, {'name': 'Switzerland', 'coordinates': {'lat': 46.818188, 'long': 8.227512}}, {'name': 'Chile', 'coordinates': {'lat': -35.675147, 'long': -71.542969}}, {'name': 'Cameroon', 'coordinates': {'lat': 7.369722, 'long': 12.354722}}, {'name': 'China', 'coordinates': {'lat': 35.86166, 'long': 104.195397}}, {'name': 'Colombia', 'coordinates': {'lat': 4.570868, 'long': -74.297333}}, {'name': 'Costa Rica', 'coordinates': {'lat': 9.748917, 'long': -83.753428}}, {'name': 'Czech Republic', 'coordinates': {'lat': 49.817492, 'long': 15.472962}}, {'name': 'Germany', 'coordinates': {'lat': 51.165691, 'long': 10.451526}}, {'name': 'Denmark', 'coordinates': {'lat': 56.26392, 'long': 9.501785}}, {'name': 'Dominican Republic', 'coordinates': {'lat': 18.735693, 'long': -70.162651}}, {'name': 'Algeria', 'coordinates': {'lat': 28.033886, 'long': 1.659626}}, {'name': 'Ecuador', 'coordinates': {'lat': -1.831239, 'long': -78.183406}}, {'name': 'Egypt', 'coordinates': {'lat': 26.820553, 'long': 30.802498}}, {'name': 'Spain', 'coordinates': {'lat': 40.463667, 'long': -3.74922}}, {'name': 'Finland', 'coordinates': {'lat': 61.92411, 'long': 25.748151}}, {'name': 'France', 'coordinates': {'lat': 46.227638, 'long': 2.213749}}, {'name': 'Gabon', 'coordinates': {'lat': -0.803689, 'long': 11.609444}}, {'name': 'United Kingdom', 'coordinates': {'lat': 55.378051, 'long': -3.435973}}, {'name': 'Ghana', 'coordinates': {'lat': 7.946527, 'long': -1.023194}}, {'name': 'Greece', 'coordinates': {'lat': 39.074208, 'long': 21.824312}}, {'name': 'Guatemala', 'coordinates': {'lat': 15.783471, 'long': -90.230759}}, {'name': 'Hong Kong', 'coordinates': {'lat': 22.396428, 'long': 114.109497}}, {'name': 'Honduras', 'coordinates': {'lat': 15.199999, 'long': -86.241905}}, {'name': 'Haiti', 'coordinates': {'lat': 18.971187, 'long': -72.285215}}, {'name': 'Hungary', 'coordinates': {'lat': 47.162494, 'long': 19.503304}}, {'name': 'Indonesia', 'coordinates': {'lat': -0.789275, 'long': 113.921327}}, {'name': 'Ireland', 'coordinates': {'lat': 53.41291, 'long': -8.24389}}, {'name': 'Israel', 'coordinates': {'lat': 31.046051, 'long': 34.851612}}, {'name': 'India', 'coordinates': {'lat': 20.593684, 'long': 78.96288}}, {'name': 'Iraq', 'coordinates': {'lat': 33.223191, 'long': 43.679291}}, {'name': 'Italy', 'coordinates': {'lat': 41.87194, 'long': 12.56738}}, {'name': 'Jersey', 'coordinates': {'lat': 49.214439, 'long': -2.13125}}, {'name': 'Jamaica', 'coordinates': {'lat': 18.109581, 'long': -77.297508}}, {'name': 'Jordan', 'coordinates': {'lat': 30.585164, 'long': 36.238414}}, {'name': 'Japan', 'coordinates': {'lat': 36.204824, 'long': 138.252924}}, {'name': 'Kenya', 'coordinates': {'lat': -0.023559, 'long': 37.906193}}, {'name': 'South Korea', 'coordinates': {'lat': 35.907757, 'long': 127.766922}}, {'name': 'Kuwait', 'coordinates': {'lat': 29.31166, 'long': 47.481766}}, {'name': 'Kazakhstan', 'coordinates': {'lat': 48.019573, 'long': 66.923684}}, {'name': 'Lebanon', 'coordinates': {'lat': 33.854721, 'long': 35.862285}}, {'name': 'Sri Lanka', 'coordinates': {'lat': 7.873054, 'long': 80.771797}}, {'name': 'Luxembourg', 'coordinates': {'lat': 49.815273, 'long': 6.129583}}, {'name': 'Morocco', 'coordinates': {'lat': 31.791702, 'long': -7.09262}}, {'name': 'Monaco', 'coordinates': {'lat': 43.750298, 'long': 7.412841}}, {'name': 'Macau', 'coordinates': {'lat': 22.198745, 'long': 113.543873}}, {'name': 'Mauritius', 'coordinates': {'lat': -20.348404, 'long': 57.552152}}, {'name': 'Mexico', 'coordinates': {'lat': 23.634501, 'long': -102.552784}}, {'name': 'Malaysia', 'coordinates': {'lat': 4.210484, 'long': 101.975766}}, {'name': 'Nigeria', 'coordinates': {'lat': 9.081999, 'long': 8.675277}}, {'name': 'Netherlands', 'coordinates': {'lat': 52.132633, 'long': 5.291266}}, {'name': 'Norway', 'coordinates': {'lat': 60.472024, 'long': 8.468946}}, {'name': 'New Zealand', 'coordinates': {'lat': -40.900557, 'long': 174.885971}}, {'name': 'Panama', 'coordinates': {'lat': 8.537981, 'long': -80.782127}}, {'name': 'Peru', 'coordinates': {'lat': -9.189967, 'long': -75.015152}}, {'name': 'Philippines', 'coordinates': {'lat': 12.879721, 'long': 121.774017}}, {'name': 'Pakistan', 'coordinates': {'lat': 30.375321, 'long': 69.345116}}, {'name': 'Poland', 'coordinates': {'lat': 51.919438, 'long': 19.145136}}, {'name': 'Puerto Rico', 'coordinates': {'lat': 18.220833, 'long': -66.590149}}, {'name': 'Portugal', 'coordinates': {'lat': 39.399872, 'long': -8.224454}}, {'name': 'Paraguay', 'coordinates': {'lat': -23.442503, 'long': -58.443832}}, {'name': 'Qatar', 'coordinates': {'lat': 25.354826, 'long': 51.183884}}, {'name': 'Romania', 'coordinates': {'lat': 45.943161, 'long': 24.96676}}, {'name': 'Russia', 'coordinates': {'lat': 61.52401, 'long': 105.318756}}, {'name': 'Saudi Arabia', 'coordinates': {'lat': 23.885942, 'long': 45.079162}}, {'name': 'Sweden', 'coordinates': {'lat': 60.128161, 'long': 18.643501}}, {'name': 'Singapore', 'coordinates': {'lat': 1.352083, 'long': 103.819836}}, {'name': 'Slovakia', 'coordinates': {'lat': 48.669026, 'long': 19.699024}}, {'name': 'Senegal', 'coordinates': {'lat': 14.497401, 'long': -14.452362}}, {'name': 'El Salvador', 'coordinates': {'lat': 13.794185, 'long': -88.89653}}, {'name': 'Thailand', 'coordinates': {'lat': 15.870032, 'long': 100.992541}}, {'name': 'Tunisia', 'coordinates': {'lat': 33.886917, 'long': 9.537499}}, {'name': 'Turkey', 'coordinates': {'lat': 38.963745, 'long': 35.243322}}, {'name': 'Taiwan', 'coordinates': {'lat': 23.69781, 'long': 120.960515}}, {'name': 'Tanzania', 'coordinates': {'lat': -6.369028, 'long': 34.888822}}, {'name': 'Ukraine', 'coordinates': {'lat': 48.379433, 'long': 31.16558}}, {'name': 'Uganda', 'coordinates': {'lat': 1.373333, 'long': 32.290275}}, {'name': 'United States', 'coordinates': {'lat': 37.09024, 'long': -95.712891}}, {'name': 'Uruguay', 'coordinates': {'lat': -32.522779, 'long': -55.765835}}, {'name': 'Venezuela', 'coordinates': {'lat': 6.42375, 'long': -66.58973}}, {'name': 'Vietnam', 'coordinates': {'lat': 14.058324, 'long': 108.277199}}, {'name': 'South Africa', 'coordinates': {'lat': -30.559482, 'long': 22.937506}}, {'name': 'Zambia', 'coordinates': {'lat': -13.133897, 'long': 27.849332}}]
