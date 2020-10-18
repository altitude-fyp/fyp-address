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
        if key == "Economic Status":
            cal_economic_status = economic_status_1(value["employed_female"] + value["employed_male"], value["unemployed_female"] + value["unemployed_male"])
            eleven_factors.append(cal_economic_status)
        elif key == "Education Attending":
        #    print(value)
            cal_education_attending = education_attending_2(value["pre_primary"], value["primary"], value["secondary"], value["post_secondary"], value["polytechnic"], value["prof_qualification_diploma"], value["university"])
            eleven_factors.append(cal_education_attending)
        elif key == "Household Monthly Income Work":
            cal_household_monthly_income_work = household_monthly_income_3(value["below_sgd_1000"], value["sgd_1000_to_1999"], value["sgd_2000_to_2999"], value["sgd_3000_to_3999"], value["sgd_4000_to_4999"], value["sgd_5000_to_5999"], value["sgd_6000_to_6999"], value["sgd_7000_to_7999"], value["sgd_8000_to_8999"], value["sgd_9000_to_9999"], value["sgd_10000_to_10999"] + value["sgd_11000_to_11999"] + value["sgd_12000_to_12999"] + value["sgd_13000_to_13999"] + value["sgd_14000_to_14999"] + value["sgd_15000_to_17499"] + value["sgd_17500_to_19999"] + value["sgd_20000_over"]) 
            eleven_factors.append(cal_household_monthly_income_work)
        elif key == "Industry":
            cal_industry = industry_4(value["manufacturing"], value["construction"], value["wholesale_retail_trade"], value["transportation_storage"], value["accomodation_food_services"], value["information_communications"], value["financial_insurance_services"], value["real_estate_services"], value["professional_services"], value["admin_support_services"], value["public_admin_education"], value["health_social_services"], value["arts_entertainment_recreation"], value["other_comm_social_personal"], value["others"], value["hotels_restaurants"], value["transport_communications"], value["business_services"], value["other_services_industries"])
            eleven_factors.append(cal_industry)
        elif key == "Marital Status":
            cal_marital_status = marital_status_5(value["single_male"] + value["single_female"], value["married_male"] + value["married_female"], value["widowed_male"] + value["widowed_female"], value["widowed_male"] + value["widowed_female"])
            eleven_factors.append(cal_marital_status)
        elif key == "Mode Of Transport School": 
            cal_mode_of_transport = mode_of_transport_6(value["bus"], value["mrt"], value["mrt_bus"], value["mrt_car"], value["mrt_other"], value["taxi"], value["car"], value["pvt_chartered_bus"], value["lorry_pickup"], value["motorcycle_scooter"], value["others"])
            eleven_factors.append(cal_mode_of_transport)
        elif key == "Occupation":
            cal_occupation = occupation_7(value["senior_officials_managers"], value["professionals"], value["associate_professionals_tech"], value["clerical"], value["service_sales"], value["agricultural_fishery"], value["production_craftsmen"], value["plant_machine_operators"], value["cleaners_labourers"], value["workers_not_classified"])
            eleven_factors.append(cal_occupation)
        elif key == "Population Age Group":
            cal_population_age_group = population_age_group_8(value["age_0_4_total"], value["age_5_9_total"], value["age_10_14_total"], value["age_15_19_total"], value["age_20_24_total"], value["age_25_29_total"], value["age_30_34_total"], value["age_35_39_total"], value["age_40_44_total"], value["age_45_49_total"], value["age_50_54_total"], value["age_55_59_total"], value["age_60_64_total"], value["age_65_69_total"], value["age_70_74_total"], value["age_75_79_total"], value["age_80_84_total"], value["age_85_over_total"])
            eleven_factors.append(cal_population_age_group)
        elif key == "Tenancy":
            cal_tenancy = tenancy_9(value["owner"], value["tenant"], value["others"])
            eleven_factors.append(cal_tenancy)
        elif key == "Type Of Dwelling Household":
            cal_type_of_dwelling_household = type_of_household_10(value["hdb_1_and_2_room_flats"], value["hdb_3_room_flats"], value["hdb_4_room_flats"], value["hdb_5_room_and_executive_flats"], value["condominiums_and_other_apartments"], value["landed_properties"])
            eleven_factors.append(cal_type_of_dwelling_household)
        elif key == "Type Of Dwelling Pop":
            cal_type_of_dwelling_pop = type_of_household_population_11(value["hdb_1_and_2_room_flats"], value["hdb_3_room_flats"], value["hdb_4_room_flats"], value["hdb_5_room_and_executive_flats"], value["condominiums_and_other_apartments"], value["landed_properties"])
            eleven_factors.append(cal_type_of_dwelling_pop)
    return eleven_factors
             
if __name__ == "__main__":
    print("Generate finance indicators")
    generate_finance()
    print("\n\ndone\n")
