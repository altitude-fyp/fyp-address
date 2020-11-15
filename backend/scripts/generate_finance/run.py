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
    risk_aversion_list =[]
    utility_list = []
    optimaly_list = []
    risk_free_weight_list = []
    product_category_list = []
    citi_product_list = []
    risky_values_graph_1 = []
    utility_values_graph_1 = []
    standard_deviation_graph_2 = []
    expected_returns_graph_2 = []

    # Get Data from Onemap (all regions)
    for i in onemap_collection.find():
        region = i["_id"]
        region_data = i["data"]

        # Calculation for 1 region
        eleven_factors = calculate_eleven_factors(region_data)
        # print(str(region) + ": " + str(eleven_factors))

        # Calculate risk_aversion
        risk_aversion = risk_aversion_12(eleven_factors)
        # print(str(region) + ": " + str(risk_aversion))

    #     # Calculate utility value
        utility = calculate_utility(risk_aversion)
    #     # print("utility value: " + str(utility))

    #     # Calculate optimal_y
        optimal_y = calculate_optimal_y(risk_aversion)
    #     # print("optimal_y value: " + str(optimal_y))

        # Product Category
        product_cat = product_category(optimal_y[0])
        # print("cat:" + str(product_cat))

        # Product List
        products = citi_products(product_cat)
        # print(str(region) + ": " + str(products))

        utility_full = utility_to_risky(risk_aversion)

        indifference_full = indifference_curve(risk_aversion)

        # Things that we want to show on FE
        region_list.append(region) # Region information
        risk_aversion_list.append(risk_aversion) # Will be useful to show 
        utility_list.append(utility) # Not useful to show since the values are all weird cos of the data 
        optimaly_list.append(optimal_y[0]) # Show in the frontend in percentange 
        risk_free_weight_list.append(optimal_y[1]) # Show in the frontend in percentage 
        product_category_list.append(product_cat) # No need to show in frontend 
        citi_product_list.append(products) # Show the list of citi products for the region 

        risky_values_graph_1.append(utility_full[0])
        utility_values_graph_1.append(utility_full[1])

        standard_deviation_graph_2.append(indifference_full[0])
        expected_returns_graph_2.append(indifference_full[1])

    #   break

    df = pd.DataFrame({
        "region": region_list,
        "risk_aversion": risk_aversion_list,
        "utility": utility_list,
        "optimal_y": optimaly_list,
        "risk_free_weight": risk_free_weight_list,
        "product_category": product_category_list, 
        "citi_products": citi_product_list,
        "graph_1_x": risky_values_graph_1,
        "graph_1_y": utility_values_graph_1,
        "graph_2_x": standard_deviation_graph_2,
        "graph_2_y": expected_returns_graph_2
    })
    
    df.to_csv('scripts/generate_finance/finance.csv', index=False) 

def calculate_eleven_factors(region_data):
    # Calculate list of eleven factors
    eleven_factors = []
    for key, value in region_data.items():

        if key == "Economic Status":
            cal_economic_status = economic_status_1(value["employed_female"] + value["employed_male"], value["unemployed_female"] + value["unemployed_male"])
            eleven_factors.append(cal_economic_status)
        
        elif key == "Education Attending": 
            
            cal_education_attending = education_attending_2(
                value.get("pre_primary",0),
                value.get("primary",0),
                value.get("secondary",0),
                value.get("post_secondary",0),
                value.get("polytechnic",0),
                value.get("prof_qualification_diploma",0),
                value.get("university",0)
            )

            eleven_factors.append(cal_education_attending)
        
        elif value and key == "Household Monthly Income Work":
            
            val_10k_n_over = [
                value.get("sgd_10000_to_10999", 0),
                value.get("sgd_11000_to_11999", 0),
                value.get("sgd_12000_to_12999",0),
                value.get("sgd_13000_to_13999",0),
                value.get("sgd_14000_to_14999",0),
                value.get("sgd_15000_to_17499",0),
                value.get("sgd_17500_to_19999",0),
                value.get("sgd_20000_over",0)
            ]

            val_10k_n_over = sum([i for i in val_10k_n_over if i is not None])

            cal_household_monthly_income_work = household_monthly_income_3(
                value.get("below_sgd_1000",0),
                value.get("sgd_1000_to_1999",0),
                value.get("sgd_2000_to_2999",0),
                value.get("sgd_3000_to_3999",0),
                value.get("sgd_4000_to_4999",0),
                value.get("sgd_5000_to_5999",0),
                value.get("sgd_6000_to_6999",0),
                value.get("sgd_7000_to_7999",0),
                value.get("sgd_8000_to_8999",0),
                value.get("sgd_9000_to_9999",0),
                0
                
            ) 
            
            eleven_factors.append(cal_household_monthly_income_work)
        
        elif key == "Industry":
            cal_industry = industry_4(
                value.get("manufacturing",0),
                value.get("construction",0),
                value.get("wholesale_retail_trade",0),
                value.get("transportation_storage",0),
                value.get("accomodation_food_services",0),
                value.get("information_communications",0),
                value.get("financial_insurance_services",0),
                value.get("real_estate_services",0),
                value.get("professional_services",0),
                value.get("admin_support_services",0),
                value.get("public_admin_education",0),
                value.get("health_social_services",0),
                value.get("arts_entertainment_recreation",0),
                value.get("other_comm_social_personal",0),
                value.get("others",0),
                value.get("hotels_restaurants",0),
                value.get("transport_communications",0),
                value.get("business_services",0),
                value.get("other_services_industries",0)
            )
            eleven_factors.append(cal_industry)
        
        elif key == "Marital Status":
            cal_marital_status = marital_status_5(
                value.get("single_male",0) + value.get("single_female",0),
                value.get("married_male",0) + value.get("married_female",0),
                value.get("widowed_male",0) + value.get("widowed_female",0),
                value.get("widowed_male",0) + value.get("widowed_female",0)
            )
            eleven_factors.append(cal_marital_status)
        
        elif value and key == "Mode Of Transport School": 
            cal_mode_of_transport = mode_of_transport_6(
                value.get("bus",0),
                value.get("mrt",0),
                value.get("mrt_bus",0),
                value.get("mrt_car",0),
                value.get("mrt_other",0),
                value.get("taxi",0),
                value.get("car",0),
                value.get("pvt_chartered_bus",0),
                value.get("lorry_pickup",0),
                value.get("motorcycle_scooter",0),
                value.get("others",0)
            )
            eleven_factors.append(cal_mode_of_transport)

        elif key == "Occupation":

            cal_occupation = occupation_7(
                value.get("senior_officials_managers",0), 
                value.get("professionals",0), 
                value.get("associate_professionals_tech",0), 
                value.get("clerical"),
                value.get("service_sales",0), 
                value.get("agricultural_fishery",0), 
                value.get("production_craftsmen",0), 
                value.get("plant_machine_operators",0), 
                value.get("cleaners_labourers",0), 
                value.get("workers_not_classified",0)
            )

            eleven_factors.append(cal_occupation)

        elif key == "Population Age Group":

            cal_population_age_group = population_age_group_8(
                value.get("age_0_4_total",0), 
                value.get("age_5_9_total",0), 
                value.get("age_10_14_total",0), 
                value.get("age_15_19_total",0), 
                value.get("age_20_24_total",0), 
                value.get("age_25_29_total",0), 
                value.get("age_30_34_total",0), 
                value.get("age_35_39_total",0), 
                value.get("age_40_44_total",0), 
                value.get("age_45_49_total",0), 
                value.get("age_50_54_total",0), 
                value.get("age_55_59_total",0), 
                value.get("age_60_64_total",0), 
                value.get("age_65_69_total",0), 
                value.get("age_70_74_total",0), 
                value.get("age_75_79_total",0), 
                value.get("age_80_84_total",0), 
                value.get("age_85_over_total",0)
            )

            eleven_factors.append(cal_population_age_group)

        elif value and key == "Tenancy":

            cal_tenancy = tenancy_9(
                value.get("owner",0), 
                value.get("tenant",0), 
                value.get("others",0)
            )
            
            eleven_factors.append(cal_tenancy)

        elif value and key == "Type Of Dwelling Household":

            cal_type_of_dwelling_household = type_of_household_10(
                value.get("hdb_1_and_2_room_flats",0), 
                value.get("hdb_3_room_flats",0), 
                value.get("hdb_4_room_flats",0), 
                value.get("hdb_5_room_and_executive_flats",0), 
                value.get("condominiums_and_other_apartments",0), 
                value.get("landed_properties",0)
            )
            
            eleven_factors.append(cal_type_of_dwelling_household)

        elif key == "Type Of Dwelling Pop":

            cal_type_of_dwelling_pop = type_of_household_population_11(
                value.get("hdb_1_and_2_room_flats",0), 
                value.get("hdb_3_room_flats",0), 
                value.get("hdb_4_room_flats",0), 
                value.get("hdb_5_room_and_executive_flats",0), 
                value.get("condominiums_and_other_apartments",0), 
                value.get("landed_properties",0)
            )

            eleven_factors.append(cal_type_of_dwelling_pop)

    return eleven_factors
             
if __name__ == "__main__":
    print("Generate finance indicators")
    generate_finance()
    print("\n\ndone\n")
