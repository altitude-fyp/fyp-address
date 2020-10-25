# Sequence to call the functions in 
# 1. Call all the functions from 1 to 11
# 2. Call the risk aversion function to sum all 11 factors 
# 3. Calculate a single utility value 
# 4. Plot the graphs for each region using the points in utility graph 

# Calculating the data for OneMap to get the results 
# Economic Status (1)
def economic_status_1(employed, unemployed):
    if employed + unemployed == 0:
        return 0
    result = unemployed / (unemployed + employed)

    if result < 0.02: 
        bin1 = 0 
    elif result < 0.04: 
        bin1 = 20
    elif result < 0.06: 
        bin1 = 40
    elif result < 0.08: 
        bin1 = 60 
    elif result < 0.010:
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.10)

# Education Attending (2)
def education_attending_2(pre_primary, primary, secondary, post_secondary, polytechnic, prof_qualification_diploma, university):
    num = pre_primary + primary + secondary + post_secondary
    den = pre_primary + primary + secondary + post_secondary + polytechnic + prof_qualification_diploma + university
    if den == 0:
        return 0
    result = num / den

    if result < 0.65: 
        bin1 = 0 
    elif result < 0.70: 
        bin1 = 20
    elif result < 0.75: 
        bin1 = 40
    elif result < 0.80: 
        bin1 = 60 
    elif result < 0.85: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.05)

# Household Monthly Income (3)
def household_monthly_income_3(below_sgd_1000, sgd_1000, sgd_2000, sgd_3000, sgd_4000, sgd_5000, sgd_6000, sgd_70009, sgd_8000, sgd_9000, sgd_10000_over):

    num = sum([i for i in [below_sgd_1000, sgd_1000, sgd_2000, sgd_3000, sgd_4000, sgd_5000] if i is not None])
    den = sum([i for i in [below_sgd_1000, sgd_1000, sgd_2000, sgd_3000, sgd_4000, sgd_5000, sgd_6000, sgd_70009, sgd_8000, sgd_9000, sgd_10000_over] if i is not None])

    if den == 0:
        return 0

    result = num / den
    
    if result < 0.10: 
        bin1 = 0 
    elif result < 0.15: 
        bin1 = 20
    elif result < 0.20: 
        bin1 = 40
    elif result < 0.25: 
        bin1 = 60 
    elif result < 0.30: 
        bin1 = 80
    else: 
        bin1 = 100 

    return (bin1/100 * 0.20)

# Industry (4) 
def industry_4(manufacturing, construction, wholesale_retail_trade, transportation_storage, accomodation_food_services, information_communications, financial_insurance_services, real_estate_services, professional_services, admin_support_services, public_admin_education, health_social_services, arts_entertainment_recreation, other_comm_social_personal, others, hotels_restaurants, transport_communications, business_services, other_services_industries): 
    num = manufacturing + construction + wholesale_retail_trade + transportation_storage + accomodation_food_services + information_communications + real_estate_services + admin_support_services + public_admin_education + health_social_services + arts_entertainment_recreation + other_comm_social_personal + others + hotels_restaurants + transport_communications + business_services + other_services_industries
    den = manufacturing + construction + wholesale_retail_trade + transportation_storage + accomodation_food_services + information_communications + financial_insurance_services + real_estate_services + professional_services + admin_support_services + public_admin_education + health_social_services + arts_entertainment_recreation + other_comm_social_personal + others + hotels_restaurants + transport_communications + business_services + other_services_industries
    
    if den == 0:
        return 0    
    
    result = num / den
    
    if result < 0.65: 
        bin1 = 0 
    elif result < 0.70: 
        bin1 = 20
    elif result < 0.75: 
        bin1 = 40
    elif result < 0.80: 
        bin1 = 60 
    elif result < 0.85: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.05)

# Marital Status (5) 
def marital_status_5(single, married, widowed, divorced): 
    num = married + divorced
    den = single + married + widowed + divorced
    if den == 0:
        return 0
    result = num / den
    
    if result < 0.55: 
        bin1 = 0 
    elif result < 0.60: 
        bin1 = 20
    elif result < 0.65: 
        bin1 = 40
    elif result < 0.70: 
        bin1 = 60 
    elif result < 0.75: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.05)

# Mode of Transport to Work (6)
def mode_of_transport_6(bus, mrt, mrt_bus, mrt_car, mrt_other, taxi, car, pvt_chartered_bus, lorry_pickup, motorcycle_scooter, others): 
    num =  bus + mrt + mrt_bus + mrt_car + mrt_other + taxi + pvt_chartered_bus + lorry_pickup + motorcycle_scooter + others 
    den =  bus + mrt + mrt_bus + mrt_car + mrt_other + taxi + car + pvt_chartered_bus + lorry_pickup + motorcycle_scooter + others 
    
    if den == 0:
        return 0 

    result = num / den

    if result < 0.30: 
        bin1 = 0 
    elif result < 0.40: 
        bin1 = 20
    elif result < 0.50: 
        bin1 = 40
    elif result < 0.60: 
        bin1 = 60 
    elif result < 0.70: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.10)

# Occupation (7)
def occupation_7(senior_officials_managers, professionals, associate_professionals_tech, clerical, service_sales, agricultural_fishery, production_craftsmen, plant_machine_operators, cleaners_labourers , workers_not_classified):
    num = associate_professionals_tech + clerical + service_sales + agricultural_fishery + production_craftsmen + plant_machine_operators + cleaners_labourers + workers_not_classified 
    den = senior_officials_managers + professionals + associate_professionals_tech + clerical + service_sales + agricultural_fishery + production_craftsmen + plant_machine_operators + cleaners_labourers + workers_not_classified 
    result = num / den
    if den == 0:
        return 0    
    if result < 0.30: 
        bin1 = 0 
    elif result < 0.40: 
        bin1 = 20
    elif result < 0.50: 
        bin1 = 40
    elif result < 0.60: 
        bin1 = 60 
    elif result < 0.70: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.10)

# Population (8)
def population_age_group_8(age_0_4, age_5_9, age_10_14, age_15_19, age_20_24, age_25_29, age_30_34, age_35_39, age_40_44, age_45_49, age_50_54, age_55_59, age_60_64, age_65_69, age_70_74, age_75_79, age_80_84, age_85_over):
    num = age_0_4 + age_5_9 + age_10_14 + age_15_19 + age_40_44 + age_45_49 + age_50_54 + age_55_59 + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_85_over
    den = age_0_4 + age_5_9 + age_10_14 + age_15_19 + age_20_24 + age_25_29 + age_30_34 + age_35_39 + age_40_44 + age_45_49 + age_50_54 + age_55_59 + age_60_64 + age_65_69 + age_70_74 + age_75_79 + age_80_84 + age_85_over
    result = num / den
    if den == 0:
        return 0    
    if result < 0.70: 
        bin1 = 0 
    elif result < 0.75: 
        bin1 = 20
    elif result < 0.80: 
        bin1 = 40
    elif result < 0.85: 
        bin1 = 60 
    elif result < 0.90: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.10)

# Tenancy (9)
def tenancy_9(owner, tenant, others): 
    num = tenant + others
    den = owner + tenant + others
    result = num / den
    if den == 0:
        return 0    
    if result < 0.05: 
        bin1 = 0 
    elif result < 0.10: 
        bin1 = 20
    elif result < 0.15: 
        bin1 = 40
    elif result < 0.20: 
        bin1 = 60 
    elif result < 0.25: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.10)

# Household (10)
def type_of_household_10(hdb_1_2_room_flats, hdb_3_room_flats, hdb_4_room_flats, hdb_5_room_executive_flats, condominiums, landed_properties):
    num = hdb_1_2_room_flats + hdb_3_room_flats + hdb_4_room_flats
    den = hdb_1_2_room_flats + hdb_3_room_flats + hdb_4_room_flats + hdb_5_room_executive_flats + condominiums + landed_properties
    result = num / den
    if den == 0:
        return 0   
    if result < 0.20: 
        bin1 = 0 
    elif result < 0.30: 
        bin1 = 20
    elif result < 0.40: 
        bin1 = 40
    elif result < 0.50: 
        bin1 = 60 
    elif result < 0.60: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.07)

# Household Type (11)
def type_of_household_population_11(hdb_1_2_room_flats, hdb_3_room_flats, hdb_4_room_flats, hdb_5_room_executive_flats, condominiums, landed_properties):
    num = hdb_1_2_room_flats + hdb_3_room_flats + hdb_4_room_flats
    den = hdb_1_2_room_flats + hdb_3_room_flats + hdb_4_room_flats + hdb_5_room_executive_flats + condominiums + landed_properties
    result = num / den
    if den == 0:
        return 0    
    if result < 0.20: 
        bin1 = 0 
    elif result < 0.30: 
        bin1 = 20
    elif result < 0.40: 
        bin1 = 40
    elif result < 0.50: 
        bin1 = 60 
    elif result < 0.60: 
        bin1 = 80
    else:
        bin1 = 100 
    return (bin1/100 * 0.08)

# Sum all of the 11 factors and convert to risk aversion range (12)
def risk_aversion_12(list_1):
    total = 0 
    
    for i in list_1:
        total += i
    A = total * 3 

    if A < 0:
        A = 0 
    elif A > 5: 
        A = 5 
    return A  

# Utility Value (13)
def calculate_utility(a): 
    e = 0.12
    sd = 0.05
    sf = 0.5
    u = e - (sf * sd**2 * a)
    return (u)

# Returns CAL x and y data points with slope value (SKIP FOR NOW)
def cal (x = [0, 0.26], y = [0.07, 0.12]): 
    from scipy.stats import linregress
    stats = linregress(x, y)
    sharpe = stats[0]
    return (x, y, sharpe)

# Expected Return with weight in Risky Assets (Chart: 15)
def expected_return (): 
    e = 0.12
    rf = 0.07
    
    risky = [0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # x axis
    expected_returns = [] # y axis 
    for y in risky:
        risk_free = 1 - y
        er = e * y + risk_free * rf
        expected_returns.append(er)
    return(risky, expected_returns)

# Returns the data points for 'Utility as a Function of Allocation to Risky Asset' (Chart: 16)
def utility_to_risky (a): 
    e = 0.12
    rf = 0.07
    r_sd = 0.26
    rf_sd = 0.00
    sf = 0.5
    
    risky = [0, 0.1 , 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1] # x axis
    utility_values = [] # y axis 
    for y in risky:
        risk_free = 1 - y
        er = e * y + risk_free * rf
        sd = r_sd * y + risk_free * rf_sd 
        u = er - (sf * sd**2 * a)
        utility_values.append(u)
    return(risky, utility_values)

# Optimal_y (14)
# Returns you the optimal y and risk free weight
# This point can be highlighted on the graph 
def calculate_optimal_y (a): 
    # Values here need to be the same as on top 
    if a == 0:
        return (0, 0)

    p_e = 0.12
    rf = 0.07
    p_sd = 0.26
    
    optimal_y = (p_e - rf) / (a * p_sd**2)
    risk_free_weight = 1 - optimal_y
    
    return (optimal_y, risk_free_weight)

# Indifference Curve based on the highest utility (Chart: 17)
def indifference_curve (u, a): 
    # At standard deviation of 0, U = rf
    rf = 0.07
    sd_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    sf = 0.5
    
    new_rate = []
    
    for sd in sd_list: 
        rate = rf + (sf * sd**2 * a)
        new_rate.append(rate)
    return (sd_list, new_rate)

