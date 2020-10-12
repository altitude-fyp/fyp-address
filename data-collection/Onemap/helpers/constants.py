YEAR = "2015"

ENDPOINT = "https://developers.onemap.sg/privateapi/popapi"

PLANNING_AREA_URL = ENDPOINT + "/getPlanningareaNames"

features = [
    "/getEconomicStatus",
    "/getEducationAttending",
    "/getEthnicGroup",
    "/getHouseholdMonthlyIncomeWork",
    "/getHouseholdSize",
    "/getHouseholdStructure",
    "/getIncomeFromWork",
    "/getIndustry",
    "/getLanguageLiterate",
    "/getMaritalStatus",
    "/getModeOfTransportSchool",
    "/getOccupation",
    "/getPopulationAgeGroup",
    "/getReligion",
    "/getSpokenAtHome",
    "/getTenancy",
    "/getTypeOfDwellingHousehold",
    "/getTypeOfDwellingPop",
]

def transform(string):
    string = string[4:]
    out = ""

    for ch in string:
        if ch.upper() == ch:
            out += " " + ch
        else:
            out += ch
    
    return out.strip()

POPULATION_ENDPOINTS = {transform(f): ENDPOINT + f for f in features}

