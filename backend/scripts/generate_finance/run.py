import sys
here = sys.path[0]

sys.path.append(here[:-len("/scripts/generate_finance")])

from helpers import * 
from mongodb_helper import *
import pandas as pd

def generate_finance():
    db = get_database()
    onemap_collection = db["onemap"]

    region_list = []
    utility_list = []
    optimaly_list = []
    risk_free_weight_list = []
    # Get Data from Onemap (all regions)
    for i in onemap_collection.find():
        region = i["_id"]
        region_data = i["data"]

        # Calculation for 1 region
        eleven_factors = calculate_eleven_factors(region_data)
        # print("eleven_factors value: " + str(eleven_factors))

        # Calculate risk_aversion
        risk_aversion = risk_aversion_12(eleven_factors)
        # print("risk_aversion value: " + str(risk_aversion))

        # Calculate utility value
        utility = calculate_utility(risk_aversion)
        # print("utility value: " + str(utility))

        # Calculate optimal_y
        optimal_y = calculate_optimal_y(risk_aversion)
        # print("optimal_y value: " + str(optimal_y))

        region_list.append(region)
        utility_list.append(utility)
        optimaly_list.append(optimal_y[0])
        risk_free_weight_list.append(optimal_y[1])

    df = pd.DataFrame(region = region_list, utility = utility_list, optimal_y = optimaly_list, risk_free_weight = risk_free_weight_list)
    
    df.to_csv('finance.csv') 

def calculate_eleven_factors(region_data):
    # Calculate list of eleven factors
    eleven_factors = []
    for key, value in region_data.items():
        # if key == "Economic Status":
        #     cal_economic_status = economic_status_1(value["employed_female"] + value["employed_male"], value["unemployed_female"] + value["unemployed_male"])
        #     eleven_factors.append(cal_economic_status)
        # elif key == "Education Attending":
        if key == "Education Attending":
            print(value)
            cal_education_attending = education_attending_2(value["pre_primary"], value["primary"], value["secondary"], value["post_secondary"], value["polytechnic"], value["prof_qualification_diploma"], value["university"])
            eleven_factors.append(cal_education_attending)
        # elif key == "Household Monthly Income Work":
        #    cal_household_monthly_income_work = household_monthly_income_3(value["below_sgd_1000"], value["sgd_1000_to_1999"], value["sgd_2000_to_2999"], value["sgd_3000_to_3999"], value["sgd_4000_to_4999"], value["sgd_5000_to_5999"], value["sgd_6000_to_6999"], value["sgd_7000_to_7999"], value["sgd_8000_to_8999"], value["sgd_9000_to_9999"], value["sgd_10000_to_10999"] + value["sgd_11000_to_11999"] + value["sgd_12000_to_12999"] + value["sgd_13000_to_13999"] + value["sgd_14000_to_14999"] + value["sgd_15000_to_17499"] + value["sgd_17500_to_19999"] + value["sgd_20000_over"]) 
        #    eleven_factors.append(cal_household_monthly_income_work)
        # elif key == "Education Attending":
        #    c
    return eleven_factors
             
if __name__ == "__main__":
    print("Generate finance indicators")
    generate_finance()
    print("\n\ndone\n")
