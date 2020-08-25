YEAR = "2010"

PROTOCOL = "https://"
DOMAIN = "developers.onemap.sg"
SUBDOMAIN_POP_AREA = "/privateapi/popapi"

GET_PLANNING_AREA = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getPlanningareaNames"

GET_ECONOMIC_STATUS = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getEconomicStatus"
GET_EDUCATION_ATTENDING = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getEducationAttending"
GET_ETHNIC_GROUP = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getEthnicGroup"
GET_HOUSEHOLD_MONTHLY_INCOME_WORK = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getHouseholdMonthlyIncomeWork"
GET_HOUSEHOLD_SIZE = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getHouseholdSize"
GET_HOUSEHOLD_STRUCTURE = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getHouseholdStructure"
GET_INCOME_FROM_WORK = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getIncomeFromWork"
GET_INDUSTRY = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getIncomeFromWork"
GET_LANGUAGE_LITERATE = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getLanguageLiterate"
GET_MARITAL_STATUS = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getMaritalStatus"
GET_MODE_OF_TRANSPORT_SCHOOL = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getModeOfTransportSchool"
GET_OCCUPATION = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getOccupation"
GET_POPULATION_AGE_GROUP = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getPopulationAgeGroup"
GET_RELIGION = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getReligion"
GET_SPOKEN_AT_HOME = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getSpokenAtHome"
GET_TENANCY = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getTenancy"
GET_TYPE_OF_DWELLING_HOUSEHOLD = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getTypeOfDwellingHousehold"
GET_TYPE_OF_DWELLING_POP = PROTOCOL + DOMAIN + SUBDOMAIN_POP_AREA + "/getTypeOfDwellingPop"

URL_LIST_POP_AREA = {
    "economicStatus" : GET_ECONOMIC_STATUS,
    "educationAttending": GET_EDUCATION_ATTENDING,
    "ethnicGroup": GET_ETHNIC_GROUP, 
    "householdMonthlyIncome":GET_HOUSEHOLD_MONTHLY_INCOME_WORK,
    "householdSize": GET_HOUSEHOLD_SIZE,
    "householdStructure": GET_HOUSEHOLD_STRUCTURE,
    "incomeFromWork": GET_INCOME_FROM_WORK,
    "industry": GET_INDUSTRY,
    "languageLiterate": GET_LANGUAGE_LITERATE,
    "maritalStatus": GET_MARITAL_STATUS,
    "modeOfTransportationSchool": GET_MODE_OF_TRANSPORT_SCHOOL,
    "occupation": GET_OCCUPATION,
    "populationAgeGroup": GET_POPULATION_AGE_GROUP,
    "religion": GET_RELIGION,
    "spokenAtHome": GET_SPOKEN_AT_HOME,
    "tenancy": GET_TENANCY,
    "typeOfDwellingHousehold": GET_TYPE_OF_DWELLING_HOUSEHOLD,
    "typeOfDwellingPop": GET_TYPE_OF_DWELLING_POP
}