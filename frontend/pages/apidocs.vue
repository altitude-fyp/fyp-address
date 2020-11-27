<template>

  <v-app style="padding-top: 50px">
    <v-container>


              <div class="nplTitle" align="center">API Documentation</div>

    <v-card>

      <v-tabs
        background-color="grey lighten-4"
        dense
        vertical>

        <v-tab>
          Explore the APIs
        </v-tab>

        <v-tab>
          Response Formats
        </v-tab>



        <!--Documentation for #Explore the APIs goes here-->
        <v-tab-item>

          <v-card flat>
            <v-card-text>
              <!--/api/address CODE BLOCK-->
              <div style="padding-left: 10px">

              The Citi Address Analytics Tool APIs (Application Programming Interfaces) power its platform for communications. Behind these APIs is a software layer connecting and optimizing communications networks around the world to allow Citi employees to connect to their existing Citi applications for data augmentation purposes.


              The APIs were built with Python FastAPI and served over Uvicorn. It is now temporarily deployed on an AWS Ubuntu 18.04 EC2 instance, served through Nginx. <br><br>


              You can make a raw HTTP request in your code (for example, using a module like got in Python) or by using a tool like Postman. CAAT uses mostly GET, POST methods.

              <h3>/api/address - Get Address Data</h3>
              Input: Customer Addresses
              Output: Country Data + Region Data + Analytics

              For more information, please refer to the individual data source documentation.
              </div>
              <!-- Code Tabs and Scripts are in here-->
              <v-tabs fixed-tabs>
                <v-tab>PYTHON</v-tab>
                <v-tab>CURL</v-tab>
                <v-tab>NODEJS</v-tab>

                <!-- Scripts are below-->
                <!--Python script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <pre v-highlightjs>
                        <code class="python">
1 import requests
2 url = "{{API_URL}}/api/address/"
3 payload  = {"address": "1234567"}
4 headers= {}
5 response = requests.request("HEAD", url, headers=headers, data = payload)
6 print(response.text.encode('utf8'))
                        </code>
                      </pre>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!--CURL script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
                        <pre v-highlightjs><code class="python">
1 curl --location --head '{{API_URL}}/api/address' \
2 --data-raw '{
3     "address": "1234567",
4 }'

                          </code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!-- NodeJS script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="javascript">
1  var raw = "{"address": "1234567"}";
2
3  var requestOptions = {
4  method: 'HEAD',
5  body: raw,
6  redirect: 'follow'
7  };
8
9  fetch("{{API_URL}}/api/address", requestOptions)
10  .then(response => response.text())
11  .then(result => console.log(result))
12  .catch(error => console.log('error', error));
</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
              </v-tabs>

              <!--/api/CSV CODE BLOCK-->
              <div style="padding-left: 10px">
                <h3>/api/csv - Get CSV</h3>
                Input: Raw CSV
                Output: CSV with analytics appended as additional columns

              </div>
              <!-- Code Tabs and Scripts are in here-->
              <v-tabs fixed-tabs>
                <v-tab>PYTHON</v-tab>
                <v-tab>CURL</v-tab>
                <v-tab>NODEJS</v-tab>

                <!-- Scripts are below-->
                <!--Python script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <pre v-highlightjs><code class="python">
1 import requests
2 url = "{{API_URL}}/api/csv"
3 payload  = {}
4 headers= {}
5 response = requests.request("HEAD", url, headers=headers, data = payload)
6 print(response.text.encode('utf8'))

              </code></pre>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!--CURL script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="python">
1 curl --location --head '{{API_URL}}/api/csv' \
2 --data-raw ''


</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!-- NodeJS script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="javascript">
1 var raw = "";
2 var requestOptions = {
3   method: 'HEAD',
4   body: raw,
5   redirect: 'follow'
6 };
7 fetch("{{API_URL}}/api/csv", requestOptions)
8   .then(response => response.text())
9   .then(result => console.log(result))
10   .catch(error => console.log('error', error));

</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
              </v-tabs>

            </v-card-text>
          </v-card>
        </v-tab-item>
        <!--Documentation for #Response Formats goes here-->
        <v-tab-item>
          <v-card flat>
            <v-card-text>
              CAAT can respond to your requests with JSON Objects. See example below.

              <pre v-highlightjs><code class="python">
{
  "status": "success",
  "data": {
    "house_type": "PRIVATE",
    "region": "PUNGGOL",
    "country": "Singapore",
    "onemap_address": {
      "SEARCHVAL": "WATERTOWN",
      "BLK_NO": "81",
      "ROAD_NAME": "PUNGGOL CENTRAL",
      "BUILDING": "WATERTOWN",
      "ADDRESS": "81 PUNGGOL CENTRAL WATERTOWN SINGAPORE 828760",
      "POSTAL": "828760",
      "X": "35603.49855",
      "Y": "43213.227510000004",
      "LATITUDE": "1.407078579",
      "LONGITUDE": "103.90164240000001",
      "LONGTITUDE": "103.90164240000001"
    },
    "region_data": {
      "Economic Status": {
        "employed_male": 33000,
        "unemployed_male": 900,
        "inactive_male": 6200,
        "employed_female": 27500,
        "unemployed_female": 900,
        "inactive_female": 14500
      },
      "Education Attending": {
        "planning_area": "Punggol",
        "pre_primary": 2300,
        "primary": 9200,
        "secondary": 4300,
        "post_secondary": 800,
        "polytechnic": 1500,
        "prof_qualification_diploma": 200,
        "university": 1200,
        "year": 2015
      },
      "Ethnic Group": {
        "planning_area": "Punggol",
        "chinese": 84900,
        "malays": 14490,
        "indian": 7720,
        "others": 2690,
        "year": 2015
      },
      "Household Monthly Income Work": {
        "planning_area": "Punggol",
        "total": 33200,
        "below_sgd_1000": 600,
        "no_working_person": 1700,
        "sgd_10000_over": null,
        "sgd_10000_to_10999": 2100,
        "sgd_11000_to_11999": 1700,
        "sgd_1000_to_1999": 900,
        "sgd_12000_to_12999": 2000,
        "sgd_13000_to_13999": 1800,
        "sgd_14000_to_14999": 1700,
        "sgd_15000_to_17499": 3000,
"sgd_17500_to_19999": 2100,
        "sgd_20000_over": 1700,
        "sgd_2000_to_2999": 1600,
        "sgd_3000_to_3999": 1400,
        "sgd_4000_to_4999": 1700,
        "sgd_5000_to_5999": 1700,
        "sgd_6000_to_6999": 2000,
        "sgd_7000_to_7999": 1800,
        "sgd_8000_over": null,
        "sgd_8000_to_8999": 1700,
        "sgd_9000_to_9999": 2100,
        "year": 2015
      },
      "Household Size": {
        "planning_area": "Punggol",
        "person1": 1800,
        "person2": 7400,
        "person3": 8900,
        "person4": 9000,
        "person5": 3700,
        "person6": null,
        "person7": null,
        "person_more_8": null,
        "year": 2015
      },
      "Household Structure": {
        "planning_area": "Punggol",
        "no_family_nucleus": 2500,
        "ofn_1_gen": 5900,
        "ofn_2_gen": 21200,
        "ofn_3_more_gen": 1800,
        "tfn_1to2_gen": null,
        "tfn_3_more_gen": null,
        "three_more_fam_nucleus": null,
        "year": 2015
      },
      "Income From Work": {
        "planning_area": "Punggol",
        "below_sgd_1000": 3600,
        "sgd_1000_to_1499": 3200,
        "sgd_1500_to_1999": 2800,
        "sgd_2000_to_2499": 3000,
        "sgd_2500_to_2999": 3500,
        "sgd_3000_to_3999": 7100,
        "sgd_4000_to_4999": 6200,
        "sgd_5000_to_5999": 6100,
        "sgd_6000_to_6999": 5500,
        "sgd_7000_to_7999": 4900,

"sgd_8000_over": null,
        "year": 2015
      },
      "Industry": {
        "planning_area": "Punggol",
        "manufacturing": 6500,
        "construction": 2700,
        "wholesale_retail_trade": 10100,
        "transportation_storage": 6100,
        "accommodation_food_services": 2800,
        "information_communications": 3100,
        "financial_insurance_services": 5100,
        "real_estate_services": 1400,
        "professional_services": 5400,
        "admin_support_services": 2200,
        "public_admin_education": 8600,
        "health_social_services": 2500,
        "arts_entertainment_recreation": 1100,
        "other_comm_social_personal": 2300,
        "others": 700,
        "hotels_restaurants": 0,
        "transport_communications": 0,
        "business_services": 0,
        "other_services_industries": 0,
        "year": 2015
      },
      "Language Literate": {
        "planning_area": "Punggol",
        "no_literate": 2100,
        "l1_chi": 8600,
        "l1_eng": 7300,
        "l1_mal": 500,
        "l1_tam": 100,
        "l1_non_off": 200,
        "l2_eng_chi": 46900,
        "l2_eng_mal": 8200,
        "l2_eng_tam": 2200,
        "l2_other_two": 300,
        "l3_eng_chi_mal": null,
        "l3_eng_mal_tam": null,
        "l3_other_three": null,
        "year": 2015,
        "l2_eng_non_off": 2400
      },
      "Marital Status": {
        "single_male": 7700,
        "married_male": 30500,
        "widowed_male": 600,
 "divorced_male": 1200,
        "single_female": 7500,
        "married_female": 30700,
        "widowed_female": 2300,
        "divorced_female": 2300
      },
      "Mode Of Transport School": {
        "planning_area": "Punggol",
        "bus": 3200,
        "mrt": 900,
        "mrt_bus": 2500,
        "mrt_car": 0,
        "mrt_other": 0,
        "taxi": 0,
        "car": 2400,
        "pvt_chartered_bus": 1500,
        "lorry_pickup": 0,
        "motorcycle_scooter": 0,
        "others": 300,
        "no_transport_required": 6900,
        "year": 2015
      },
      "Occupation": {
        "planning_area": "Punggol",
        "senior_officials_managers": 9600,
        "professionals": 13900,
        "associate_professionals_tech": 14700,
        "clerical": 6800,
        "service_sales": 6000,
        "agricultural_fishery": 0,
        "production_craftsmen": 1900,
        "plant_machine_operators": 2800,
        "cleaners_labourers": 3000,
        "workers_not_classified": 0,
        "year": 2015
      },
      "Population Age Group": {
        "age_0_4_total": 12000,
        "age_5_9_total": 9200,
        "age_10_14_total": 6190,
        "age_15_19_total": 4450,
        "age_20_24_total": 3940,
        "age_25_29_total": 6750,
        "age_30_34_total": 15690,
        "age_35_39_total": 13400,
        "age_40_44_total": 10610,
        "age_45_49_total": 6500,
        "age_50_54_total": 5540,
 "age_55_59_total": 4730,
        "age_60_64_total": 3960,
        "age_65_69_total": 3020,
        "age_70_74_total": 1560,
        "age_75_79_total": 1040,
        "age_80_84_total": 660,
        "age_85_over_total": 510,
        "total_total": 109750,
        "age_0_4_male": 6140,
        "age_5_9_male": 4740,
        "age_10_14_male": 3170,
        "age_15_19_male": 2330,
        "age_20_24_male": 1940,
        "age_25_29_male": 2690,
        "age_30_34_male": 7130,
        "age_35_39_male": 6880,
        "age_40_44_male": 5630,
        "age_45_49_male": 3450,
        "age_50_54_male": 2890,
        "age_55_59_male": 2280,
        "age_60_64_male": 1830,
        "age_65_69_male": 1420,
        "age_70_74_male": 700,
        "age_75_79_male": 460,
        "age_80_84_male": 270,
        "age_85_over_male": 140,
        "total_male": 54100,
        "age_0_4_female": 5860,
        "age_5_9_female": 4460,
        "age_10_14_female": 3030,
        "age_15_19_female": 2120,
        "age_20_24_female": 2000,
        "age_25_29_female": 4060,
        "age_30_34_female": 8560,
        "age_35_39_female": 6520,
        "age_40_44_female": 4980,
        "age_45_49_female": 3050,
        "age_50_54_female": 2650,
        "age_55_59_female": 2450,
        "age_60_64_female": 2130,
        "age_65_69_female": 1600,
        "age_70_74_female": 860,
        "age_75_79_female": 580,
        "age_80_84_female": 390,
        "age_85_over_female": 380,
        "total_female": 55650
      },
      "Religion": {
"planning_area": "Punggol",
        "no_religion": 17800,
        "buddhism": 28600,
        "taoism": 7800,
        "islam": 8500,
        "hinduism": 4100,
        "sikhism": 600,
        "catholic_christian": 5500,
        "other_christians": 9600,
        "other_religions": 400,
        "year": 2015
      },
      "Spoken At Home": {
        "planning_area": "Punggol",
        "english": 38600,
        "mandarin": 34300,
        "chinese_dialects": 9500,
        "malay": 7800,
        "tamil": 2100,
        "other_indian_languages": 2300,
        "others": 500,
        "year": 2015
      },
      "Tenancy": {
        "planning_area": "Punggol",
        "owner": 31900,
        "tenant": 1300,
        "others": 0,
        "year": 2015
      },
      "Type Of Dwelling Household": {
        "planning_area": "Punggol",
        "hdb_1_and_2_room_flats": 1800,
        "hdb_3_room_flats": 1900,
        "hdb_4_room_flats": 14700,
        "hdb_5_room_and_executive_flats": 13400,
        "condominiums_and_other_apartments": 1400,
        "landed_properties": 0,
        "others": 0,
        "year": 2015,
        "total_hdb": 31800
      },
      "Type Of Dwelling Pop": {
        "planning_area": "Punggol",
        "year": 2015,
        "hdb_1_and_2_room_flats": 4660,
        "hdb_3_room_flats": 6530,
        "hdb_4_room_flats": 48970,
  "hdb_5_room_and_executive_flats": 45590,
        "condominiums_and_other_apartments": 3480,
        "landed_properties": 280,
        "others": 250,
        "total_hdb": 105740,
        "total": 109750
      }
    },
    "country_data": {
      "population density": 7687.293977,
      "population total": 5610000,
      "gdp nominal": 308051000000,
      "gdp nominal per capita": 56319,
      "gdp ppp": 452686000000,
      "gdp ppp per capita": 82762,
      "gini": 46.4,
      "hdi": 0.912,
      "intentional homicide rate": 0.16,
      "intentional homicide rate count": 9,
      "cocaine use": 0.0002,
      "total firearm death rate": 0.025,
      "firearm death rate by homicide": 0.005,
      "firearm death rate by suicide": 0.0165,
      "unintentional firearm death rate": 0.003,
      "undetermined firearm death rate": 0,
      "guns per 100 inhabitants": 0.5,
      "opiate use": 0.004,
      "suicide rate": 7.9,
      "male suicide rate": 114,
      "female suicide rate": 11.1,
      "suicide rate (male:female ratio)": 76,
      "suicide rate rank": 4.9,
      "age structure (0-14 years)": 0.15,
      "age structure (15-64 years)": 0.721,
      "age structure (over 65 years)": 0.129,
      "number of births (in thousands)": 249,
      "capital population": 5638700,
      "fertility rate": 1.1,
      "literacy rate": 0.968,
      "male literacy rate": 0.9870000000000001,
      "female literacy rate": 0.951,
      "median age": 34.6,
      "median male age": 34.5,
      "median female age": 34.7,
      "labour force": 3212000,
      "labour force (agriculture)": 0.001,
      "labour force (industry)": 0.302,
      "labour force (service)": 0.6970000000000001,
"sex ratio (at birth)": 1.07,
      "sex ratio (0-14 years)": 1.05,
      "sex ratio (15-24 years)": 0.96,
      "sex ratio (25-54 years)": 0.95,
      "sex ratio (55-64 years)": 1,
      "sex ratio (over 65 years)": 0.85,
      "sex ratio (total)": 0.96,
      "traffic-related death rate (per 100,000 inhabitants per year)": 3.6,
      "traffic-related death rate (per 100,000 motor vehicles)": 20.2,
      "traffic-related death rate (per 1 billion vehicle-km)": "",
      "traffic-related death rate (total)": 197,
      "dependency ratio (total)": 34.5,
      "dependency ratio (youth)": 16.5,
      "dependency ratio (elderly)": 18,
      "potential support ratio": 5.6,
      "GNI per capita (female)": 69508,
      "GNI per capita (male)": 95809,
      "male to female income ratio": 1.378,
      "government budget per capita": 9421,
      "oil imports": 976100,
      "net oil exports": -976100,
      "foreign exchange reserves (million USD)": 321351,
      "tariff rate": 0.0007000000000000001,
      "unemployment rate": 2.4,
      "co2 emissions (tonnes)": 9.7,
      "natural gas consumption (million m3 per year)": 12700,
      "overall mean BMI": 23.7,
      "female mean BMI": 23.2,
      "male mean BMI": 24.3,
      "infant mortality rate under 5 (per 1000 lives births)": 2.8,
      "life expectancy (overall)": 83.8,
      "life expectancy (female)": 85.8,
      "life expectancy (male)": 81.5,
      "maternal mortality rate (per 100,000 live births)": 8,
      "mortality rate (per 1000 people)": 3.42,
      "number of physicians (per 1000 people)": 19.5,
      "proportion of population using improved sanitation": 100,
      "cigarette consumption (per year per capita)": 851.2,
      "number of internet hosts": 1960000,
      "number of internet users": 4821119,
      "Unemployment rate": 2.4,
      "Consumer Prices, period average, percent change": 0.51198915968258,
      "Gross domestic product, constant prices, purchasing power parity, per capita, percent change ": 1.78764790402172,
      "Consumer Price Index, All items": 100,
  "Geographical Outreach, Number of Institutions, Other deposit takers": 27,
      "Geographical Outreach, Number of Institutions, Insurance corporations": 186,
      "Use of Financial Services, Number of Borrowers, Commercial banks": 5415481,
      "Key Indicators, Use of Financial Services, Outstanding loans from commercial banks (% of GDP)": 136.415402122712,
      "Geographical Outreach, Number of Branches, Excluding Headquarters, Commercial banks": 259,
      "Financial Development Index": 0.7528315782547,
      "Financial Institutions Access Index": 0.387628346681595,
      "Financial Institutions Depth Index": 0.932063043117523,
      "Financial Institutions Efficiency Index": 0.805092632770538,
      "Financial Institutions Index": 0.756877899169922,
      "Financial Markets Access Index": 0.836043894290924,
      "Financial Markets Depth Index": 0.895078301429749,
      "Financial Markets Efficiency Index": 0.382047742605209,
      "Financial Markets Index": 0.720229148864746,
      "Financial, Financial Soundness Indicators, Core Set, Deposit Takers, Capital Adequacy, Non-performing Loans Net of Provisions to Capital, Percent": 6.36563893797044,
      "Agricultural land (% of land area)": 0.930888592414402,
      "Agriculture, forestry, and fishing, value added (% of GDP)": 0.0296709187759584,
      "Arable land (% of land area)": 0.789844838268139,
      "Arable land (hectares per person)": 0.0000998701157733944,
      "Crop production index (2004-2006 = 100)": 132.99,
      "Employment in agriculture, female (% of female employment) (modeled ILO estimate)": 0.330000013113022,
      "Employment in agriculture, male (% of male employment) (modeled ILO estimate)": 1.00800001621246,
      "Fertilizer consumption (kilograms per hectare of arable land)": 30237.8556190309,
      "Food production index (2004-2006 = 100)": 114.9,
      "Forest area (% of land area)": 23.0606488428662,
      "Forest area (sq. km)": 163.500003814697,
      "Land area (sq. km)": 709.000015258789,
      "Livestock production index (2004-2006 = 100)": 111.93,
      "Permanent cropland (% of land area)": 0.141043722620535,
      "Rural population": 0,
      "Rural population (% of total population)": 0,
      "Surface area (sq. km)": 719.000015258789,
      "Grants, excluding technical cooperation (BoP, current US$)": 1620000,
      "Incidence of tuberculosis (per 100,000 people)": 47,
      "Maternal mortality ratio (modeled estimate, per 100,000 live births)": 8,
 "Mortality rate, under-5 (per 1,000 live births)": 2.5,
      "Net migration": 135142,
      "Prevalence of HIV, total (% of population ages 15-49)": 0.2,
      "Prevalence of stunting, height for age (% of children under 5)": 4.4,
      "Primary completion rate, total (% of relevant age group)": 99.9218292236328,
      "School enrollment, primary and secondary (gross), gender parity index (GPI)": 0.995630025863647,
      "Technical cooperation grants (BoP, current US$)": 7520000,
      "Access to electricity (% of population)": 100,
      "CO2 emissions (kt)": 37535.412,
      "CO2 emissions (metric tons per capita)": 6.69404629657536,
      "Ease of doing business index (1=most business-friendly regulations)": 2,
      "Electric power consumption (kWh per capita)": 8844.68759301201,
      "Energy use (kg of oil equivalent per capita)": 5121.80431773157,
      "Land area where elevation is below 5 meters (% of total land area)": 8.1616391,
      "Methane emissions (kt of CO2 equivalent)": 2385.8004,
      "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)": 1908.561066,
      "Population growth (annual %)": 1.14428330688929,
      "Population in urban agglomerations of more than 1 million (% of total population)": 100,
      "Population living in areas where elevation is below 5 meters (% of total population)": 10.332070593,
      "Population, total": 5703569,
      "Prevalence of underweight, weight for age (% of children under 5)": 3.3,
      "Renewable electricity output (% of total electricity output)": 1.82088664088069,
      "Renewable energy consumption (% of total final energy consumption)": 0.70863529719762,
      "Terrestrial and marine protected areas (% of total territorial area)": 2.46306282917716,
      "Total greenhouse gas emissions (kt of CO2 equivalent)": 55910.2813044732,
      "Urban population": 5703569,
      "Urban population (% of total population)": 100,
      "Adjusted net savings, including particulate emission damage (% of GNI)": 34.7026850791648,
      "Central government debt, total (% of GDP)": 109.197506171167,
      "Charges for the use of intellectual property, payments (BoP, current US$)": 16150764512.917,
 "Charges for the use of intellectual property, receipts (BoP, current US$)": 8472843450.47925,
      "Current account balance (BoP, current US$)": 63139151735.8078,
      "Expense (% of GDP)": 14.8364034354547,
      "Exports of goods and services (% of GDP)": 173.517266760671,
      "Foreign direct investment, net inflows (BoP, current US$)": 105465616772.247,
      "GDP (current US$)": 372062527488.638,
      "GDP growth (annual %)": 0.733309934559728,
      "GDP per capita (current US$)": 65233.2824392302,
      "GDP per capita growth (annual %)": -0.412794667941512,
      "GDP per capita, PPP (current international $)": 101375.775310612,
      "GNI per capita, Atlas method (current US$)": 59590,
      "GNI per capita, PPP (current international $)": 92020,
      "GNI, Atlas method (current US$)": 339860544637.511,
      "GNI, PPP (current international $)": 524841789129.782,
      "Gross capital formation (% of GDP)": 24.8591074648761,
      "Gross savings (% of GDP)": 42.8341161882636,
      "Imports of goods and services (% of GDP)": 145.631114824683,
      "Industry (including construction), value added (% of GDP)": 24.4916096906876,
      "Inflation, GDP deflator (annual %)": 0.0948660334753555,
      "Inflation, consumer prices (annual %)": 0.565260568780358,
      "PPP conversion factor, GDP (LCU per international $)": 0.877835396384707,
      "Price level ratio of PPP conversion factor (GDP) to market exchange rate": 0.643479985621395,
      "Revenue, excluding grants (% of GDP)": 18.3682281698985,
      "Total reserves (includes gold, current US$)": 285477830549.322,
      "Children out of school, primary, female": 150,
      "Children out of school, primary, male": 326,
      "Government expenditure on education, total (% of GDP)": 2.85435009002686,
      "Government expenditure on education, total (% of government expenditure)": 28.8391494750977,
      "Government expenditure per student, primary (% of GDP per capita)": 17.51811,
      "Government expenditure per student, secondary (% of GDP per capita)": 21.63771,
      "Government expenditure per student, tertiary (% of GDP per capita)": 23.54145,
      "Gross intake ratio in first grade of primary education, female (% of relevant age group)": 101.12881,
      "Gross intake ratio in first grade of primary education, male (% of relevant age group)": 100.9814,
  "Labor force, female (% of total labor force)": 41.7545466272949,
      "Labor force, total": 3527065,
      "Literacy rate, adult female (% of females ages 15 and above)": 95.9194107055664,
      "Literacy rate, adult male (% of males ages 15 and above)": 98.8508987426758,
      "Literacy rate, adult total (% of people ages 15 and above)": 97.344856262207,
      "Literacy rate, youth female (% of females ages 15-24)": 99.9423675537109,
      "Literacy rate, youth male (% of males ages 15-24)": 99.9174194335938,
      "Literacy rate, youth total (% of people ages 15-24)": 99.9296264648438,
      "Persistence to last grade of primary, female (% of cohort)": 99.3621368408203,
      "Persistence to last grade of primary, male (% of cohort)": 99.422477722168,
      "Population ages 0-14 (% of total population)": 12.3315031501445,
      "Population ages 15-64 (% of total population)": 75.2753673675391,
      "Primary completion rate, female (% of relevant age group)": 100.025909423828,
      "Primary completion rate, male (% of relevant age group)": 99.8231735229492,
      "Progression to secondary school, female (%)": 98.20661,
      "Progression to secondary school, male (%)": 100,
      "Pupil-teacher ratio, primary": 14.69428,
      "Repeaters, primary, female (% of female enrollment)": 0.13776,
      "Repeaters, primary, male (% of male enrollment)": 0.17506,
      "School enrollment, primary (% gross)": 100.261871337891,
      "School enrollment, primary (% net)": 99.66959,
      "School enrollment, primary (gross), gender parity index (GPI)": 0.999279975891113,
      "School enrollment, secondary (% gross)": 105.844299316406,
      "School enrollment, secondary (% net)": 99.78462,
      "School enrollment, tertiary (% gross)": 88.8864517211914,
      "Trained teachers in primary education (% of total teachers)": 98.2631607055664,
      "Unemployment, female (% of female labor force) (modeled ILO estimate)": 4.31400012969971,
      "Unemployment, male (% of male labor force) (modeled ILO estimate)": 3.96199989318848,
      "Unemployment, total (% of total labor force) (modeled ILO estimate)": 4.10900020599365,
     "Alternative and nuclear energy (% of total energy use)": 0.192789211552613,
      "Energy imports, net (% of energy use)": 97.6820012924571,
      "Energy intensity level of primary energy (MJ/$2011 PPP GDP)": 2.39485551302144,
      "Fossil fuel energy consumption (% of total)": 90.5788735805032,
      "Fuel exports (% of merchandise exports)": 12.5950586926204,
      "GDP per unit of energy use (constant 2017 PPP $ per kg of oil equivalent)": 17.1440878468364,
      "Ores and metals exports (% of merchandise exports)": 0.736809700513589,
      "Time required to get electricity (days)": 26,
      "Total natural resources rents (% of GDP)": 0.000187592851112122,
      "Bird species, threatened": 22,
      "Fish species, threatened": 29,
      "Mammal species, threatened": 14,
      "PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)": 19.0782564997534,
      "PM2.5 air pollution, population exposed to levels exceeding WHO guideline value (% of total)": 100,
      "Plant species (higher), threatened": 62,
      "Renewable internal freshwater resources per capita (cubic meters)": 109.694748766117,
      "Renewable internal freshwater resources, total (billion cubic meters)": 0.6,
      "Automated teller machines (ATMs) (per 100,000 adults)": 58.7772609796383,
      "Bank capital to assets ratio (%)": 9.32388396583132,
      "Bank nonperforming loans to total gross loans (%)": 1.30642223339991,
      "Broad money (% of GDP)": 124.622035641748,
      "Broad money growth (annual %)": 4.95121786918272,
      "Commercial bank branches (per 100,000 adults)": 7.81963560498081,
      "Deposit interest rate (%)": 0.1975,
      "Depth of credit information index (0=low to 8=high)": 7,
      "Domestic credit to private sector (% of GDP)": 120.780144205394,
      "Interest rate spread (lending rate minus deposit rate, %)": 5.0525,
      "International migrant stock, total": 2543638,
      "Lending interest rate (%)": 5.25,
      "Listed domestic companies, total": 470,
      "Market capitalization of listed domestic companies (% of GDP)": 187.407029325546,
 "Market capitalization of listed domestic companies (current US$)": 697271330000,
      "Official exchange rate (LCU per US$, period average)": 1.36415833333333,
      "Real interest rate (%)": 5.15024813040919,
      "Risk premium on lending (lending rate minus treasury bill rate, %)": 5.12875,
      "S&P Global Equity Indices (annual % change)": 13.5428223542043,
      "Stocks traded, total value (% of GDP)": 30.6948836720698,
      "Stocks traded, turnover ratio of domestic shares (%)": 16.3787259114755,
      "Strength of legal rights index (0=weak to 12=strong)": 8,
      "Adolescent fertility rate (births per 1,000 women ages 15-19)": 3.5134,
      "Births attended by skilled health staff (% of total)": 99.6,
      "Contributing family workers, female (% of female employment) (modeled ILO estimate)": 0.467000007629395,
      "Contributing family workers, male (% of male employment) (modeled ILO estimate)": 0.280000001192093,
      "Employment in industry, female (% of female employment) (modeled ILO estimate)": 10.6160001754761,
      "Employment in industry, male (% of male employment) (modeled ILO estimate)": 18.9409999847412,
      "Employment in services, female (% of female employment) (modeled ILO estimate)": 89.0540008544922,
      "Employment in services, male (% of male employment) (modeled ILO estimate)": 80.0510025024414,
      "Fertility rate, total (births per woman)": 1.14,
      "Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)": 61.9700012207031,
      "Labor force participation rate, male (% of male population ages 15+) (modeled ILO estimate)": 78.2979965209961,
      "Life expectancy at birth, female (years)": 85.4,
      "Life expectancy at birth, male (years)": 81,
      "Prevalence of HIV, female (% ages 15-24)": 0.1,
      "Prevalence of HIV, male (% ages 15-24)": 0.1,
      "Proportion of seats held by women in national parliaments (%)": 23,
      "Unemployment, youth female (% of female labor force ages 15-24) (modeled ILO estimate)": 12.5699996948242,
      "Unemployment, youth male (% of male labor force ages 15-24) (modeled ILO estimate)": 6.69099998474121,
      "Vulnerable employment, female (% of female employment) (modeled ILO estimate)": 6.57299995422363,
      "Vulnerable employment, male (% of male employment) (modeled ILO estimate)": 11.8750002682209,
 "Wage and salaried workers, female (% of female employment) (modeled ILO estimate)": 90.8410034179688,
      "Wage and salaried workers, male (% of male employment) (modeled ILO estimate)": 82.5009994506836,
      "Age dependency ratio (% of working-age population)": 32.8455905284947,
      "Birth rate, crude (per 1,000 people)": 8.8,
      "Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (% of total)": 22.7,
      "Cause of death, by injury (% of total)": 3.7,
      "Cause of death, by non-communicable diseases (% of total)": 73.6,
      "Completeness of death registration with cause-of-death information (%)": 66,
      "Death rate, crude (per 1,000 people)": 5,
      "Diabetes prevalence (% of population ages 20 to 79)": 5.5,
      "Hospital beds (per 1,000 people)": 2.4,
      "Immunization, DPT (% of children ages 12-23 months)": 96,
      "Immunization, measles (% of children ages 12-23 months)": 95,
      "Life expectancy at birth, total (years)": 83.1463414634146,
      "Mortality caused by road traffic injury (per 100,000 people)": 2.8,
      "Mortality rate, infant (per 1,000 live births)": 2.1,
      "Mortality rate, neonatal (per 1,000 live births)": 0.9,
      "Population ages 65 and above (% of total population)": 12.3931294823164,
      "Population, female (% of total population)": 47.6559879386866,
      "Prevalence of anemia among children (% of children under 5)": 16.9,
      "Prevalence of overweight, weight for height (% of children under 5)": 2.6,
      "Prevalence of severe wasting, weight for height (% of children under 5)": 0.5,
      "Prevalence of wasting, weight for height (% of children under 5)": 3.6,
      "Refugee population by country or territory of asylum": 5,
      "Refugee population by country or territory of origin": 39,
      "Specialist surgical workforce (per 100,000 population)": 31.45,
      "Air transport, registered carrier departures worldwide": 208787,
      "Container port traffic (TEU: 20 foot equivalent units)": 36600000,
      "Fixed broadband subscriptions (per 100 people)": 25.81001069,
      "Fixed telephone subscriptions (per 100 people)": 32.83406873,
      "Mobile cellular subscriptions (per 100 people)": 156.3778947,
 "Secure Internet servers (per 1 million people)": 122481.379641414,
      "Business extent of disclosure index (0=less disclosure to 10=more disclosure)": 10,
      "High-technology exports (% of manufactured exports)": 51.7237512889669,
      "High-technology exports (current US$)": 155446548683,
      "International tourism, expenditures (% of total imports)": 4.55020057120615,
      "International tourism, receipts (% of total exports)": 3.07876287879111,
      "Lead time to export, median case (days)": 2,
      "Lead time to import, median case (days)": 2,
      "Logistics performance index: Overall (1=low to 5=high)": 4,
      "Merchandise exports (current US$)": 390763000000,
      "Merchandise imports (current US$)": 359266000000,
      "Merchandise trade (% of GDP)": 201.586815276071,
      "Net barter terms of trade index (2000 = 100)": 86.18788792,
      "New businesses registered (number)": 43046,
      "Start-up procedures to register a business (number)": 2,
      "Start-up procedures to register a business, female (number)": 2,
      "Start-up procedures to register a business, male (number)": 2,
      "Time required to start a business (days)": 1.5,
      "Time required to start a business, female (days)": 1.5,
      "Time required to start a business, male (days)": 1.5,
      "Total tax and contribution rate (% of profit)": 21,
      "Intentional homicides (per 100,000 people)": 0.15631776484,
      "Military expenditure (% of GDP)": 3.20759455704953,
      "Military expenditure (% of general government expenditure)": 21.3822937203742,
      "Net acquisition of financial assets (% of GDP)": 13.7279528411861,
      "Net incurrence of liabilities, total (% of GDP)": 8.90393737700121,
      "Net investment in nonfinancial assets (% of GDP)": -1.01633253493381,
      "Net lending (+) / net borrowing (-) (% of GDP)": 4.82401783488464,
      "Tax revenue (% of GDP)": 13.1417170586072,
      "Patent applications, nonresidents": 10270,
      "Patent applications, residents": 1575,
      "Research and development expenditure (% of GDP)": 1.94431,
      "Researchers in R&D (per million people)": 6802.53716,
      "Scientific and technical journal articles": 11458.63,
      "Technicians in R&D (per million people)": 377.36817,
      "Trademark applications, direct nonresident": 19627,
   "Trademark applications, direct resident": 6305,
      "Employment to population ratio, 15+, total (%) (modeled ILO estimate)": 67.6399993896484,
      "GDP per person employed (constant 2017 PPP $)": 164153.70984449,
      "Population density (people per sq. km of land area)": 7952.9984184018,
      "Population in the largest city (% of urban population)": 100
    }
  }
}

              </code></pre>
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
</v-container>
  </v-app>
</template>


<script>
export default {
  name: "apidocs",
}
</script>

<style>

/*

Lightfair style (c) Tristian Kelly <tristian.kelly560@gmail.com>

*/

.hljs {
  display: block;
  overflow-x: auto;
  padding: 0.5em;
  background: #fff !important;
}

.hljs-name {
  color:#01a3a3 !important;
}

.hljs-tag,.hljs-meta {
  color:#778899 !important;
}

.hljs,
.hljs-subst {
  color: #444 !important;
}

.hljs-comment {
  color: #888888 !important;
}

.hljs-keyword,
.hljs-attribute,
.hljs-selector-tag,
.hljs-meta-keyword,
.hljs-doctag,
.hljs-name {
  font-weight: bold
}

.hljs-type,
.hljs-string,
.hljs-number,
.hljs-selector-id,
.hljs-selector-class,
.hljs-quote,
.hljs-template-tag,
.hljs-deletion {
  color: #4286f4 !important;
}

.hljs-title,
.hljs-section {
  color: #4286f4 !important;
  font-weight: bold
}

.hljs-regexp,
.hljs-symbol,
.hljs-variable,
.hljs-template-variable,
.hljs-link,
.hljs-selector-attr,
.hljs-selector-pseudo {
  color: #BC6060 !important;
}

.hljs-literal {
  color: #62bcbc !important;
}

.hljs-built_in,
.hljs-bullet,
.hljs-code,
.hljs-addition {
  color: #25c6c6 !important;
}

.hljs-meta-string {
  color: #4d99bf !important;
}

.hljs-emphasis {
  font-style: italic
}

.hljs-strong {
  font-weight: bold
}

  .nplTitle {
    color:#454545;
    font-size:28px;
    font-weight:700;
    margin-top:10px;
    margin-bottom:30px;
  }



/*!* Tomorrow Night Theme *!
!* http://jmblog.github.com/color-themes-for-google-code-highlightjs *!
!* Original theme - https://github.com/chriskempson/tomorrow-theme *!
!* http://jmblog.github.com/color-themes-for-google-code-highlightjs *!

!* Tomorrow Comment *!
.hljs-comment,
.hljs-quote {
  color: #969896;
}

!* Tomorrow Red *!
.hljs-variable,
.hljs-template-variable,
.hljs-tag,
.hljs-name,
.hljs-selector-id,
.hljs-selector-class,
.hljs-regexp,
.hljs-deletion {
  color: #cc6666;
}

!* Tomorrow Orange *!
.hljs-number,
.hljs-built_in,
.hljs-builtin-name,
.hljs-literal,
.hljs-type,
.hljs-params,
.hljs-meta,
.hljs-link {
  color: #de935f;
}

!* Tomorrow Yellow *!
.hljs-attribute {
  color: #f0c674;
}

!* Tomorrow Green *!
.hljs-string,
.hljs-symbol,
.hljs-bullet,
.hljs-addition {
  color: #b5bd68;
}

!* Tomorrow Blue *!
.hljs-title,
.hljs-section {
  color: #81a2be;
}

!* Tomorrow Purple *!
.hljs-keyword,
.hljs-selector-tag {
  color: #b294bb;
}

.hljs {
  display: block;
  overflow-x: auto;
  background: #1d1f21 !important;
  color: #c5c8c6;
  padding: 0.5em;
}

.hljs-emphasis {
  font-style: italic;
}

.hljs-strong {
  font-weight: bold;
}*/

</style>
