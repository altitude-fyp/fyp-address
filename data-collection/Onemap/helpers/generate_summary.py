def generate_summary(data):
    
    def add(*stuff):
        # automatically converts null to 0
        try: return sum(i for i in stuff if i is not None and type(i) in [int, float])
        except: return 0
    
    def add_keys(d, keys):
        # adds values of keys in dictionary d
        return add(*[d.get(k, None) for k in keys])

    out = []

    for region in data:

        rname = region["_id"]
        rdata = region["data"]
        new = {}
        errors = []

        print("generating summary for", rname, " "*30, end="\r")

        try:
            economic_status = rdata.get("Economic Status", None)
            new["Economic Status"] = {
                "Employment Rate": add_keys(economic_status, ["employed_female", "employed_male"]),
                "Unemployment Rate": add_keys(economic_status, ["unemployed_female", "unemployed_male"]),
                "Inactive Rate": add_keys(economic_status, ["inactive_female", "inactive_male"]),
            }
            
            education_attending = rdata.get("Education Attending", None)
            new["Education Attending"] = {
                "Primary": add_keys(education_attending, ["pre_primary", "primary"]),
                "Secondary": add_keys(education_attending, ["secondary"]),
                "Tertiary": add_keys(education_attending, ["post_secondary", "polytechnic"]),
                "University": add_keys(education_attending, ["university"]),
            }

            household_mongthly_income_from_work = rdata.get("Household Monthly Income Work", None)
            # below 5k, 5k to 10k, above 10k
            new["Household Monthly Income Work"] = {
                "Low [0-5000]": add_keys(household_mongthly_income_from_work, ['below_sgd_1000', 'no_working_person', 'sgd_1000_to_1999', 'sgd_2000_to_2999', 'sgd_3000_to_3999', 'sgd_4000_to_4999']),
                "Middle [5000-10000]": add_keys(household_mongthly_income_from_work, ['sgd_5000_to_5999', 'sgd_6000_to_6999', 'sgd_7000_to_7999', 'sgd_8000_over', 'sgd_8000_to_8999', 'sgd_9000_to_9999']),
                "High [10000+]": add_keys(household_mongthly_income_from_work, ['sgd_10000_to_10999', 'sgd_11000_to_11999',  'sgd_12000_to_12999', 'sgd_13000_to_13999', 'sgd_14000_to_14999', 'sgd_15000_to_17499', 'sgd_17500_to_19999'])
            }

            household_size = rdata.get("Household Size", None)
            new["Household Size"] = {
                "Small [1-3]": add_keys(household_size, ["person1", "person2", "person3"]),
                "Medium [4-6]": add_keys(household_size, ["person4", "person5", "person6"]),
                "High [7+]": add_keys(household_size, ["person7", "person_more_8"]),
            }


            income_from_work = rdata.get("Income From Work", None)
            new["Income From Work"] = {
                "Low [0-3000]": add_keys(income_from_work, ['below_sgd_1000', 'sgd_1000_to_1499', 'sgd_1500_to_1999', 'sgd_2000_to_2499', 'sgd_2500_to_2999']),
                "Middle [3000-6000]": add_keys(income_from_work, ['sgd_3000_to_3999', 'sgd_4000_to_4999', 'sgd_5000_to_5999']),
                "High [6000+]": add_keys(income_from_work, ['sgd_6000_to_6999', 'sgd_7000_to_7999', 'sgd_8000_over'])
            }

            population_age_group = rdata.get("Population Age Group", None)
            new["Population Age Group"] = {
                "0-19": add_keys(population_age_group, ['age_0_4_total', 'age_5_9_total', 'age_10_14_total', 'age_15_19_total']),
                "20-39": add_keys(population_age_group, ['age_20_24_total', 'age_25_29_total', 'age_30_34_total', 'age_35_39_total']),
                "40-59": add_keys(population_age_group, ['age_40_44_total', 'age_45_49_total', 'age_50_54_total', 'age_55_59_total']),
                "60+": add_keys(population_age_group, ['age_60_64_total', 'age_65_69_total', 'age_70_74_total', 'age_75_79_total', 'age_80_84_total', 'age_85_over_total']),
            }
                
            type_of_dwelling_household = rdata.get("Type Of Dwelling Household", None)
            new["Type Of Dwelling Household"] = {
                "HDB": type_of_dwelling_household["total_hdb"],
                "Condominiums and Apartments": type_of_dwelling_household["condominiums_and_other_apartments"],
                "Landed": type_of_dwelling_household["landed_properties"],
                "Others": type_of_dwelling_household["others"]
            }

            type_of_dwelling_pop = rdata.get("Type Of Dwelling Pop", None)
            new["Type Of Dwelling Pop"] = {
                "HDB": type_of_dwelling_pop["total_hdb"],
                "Condominiums and Apartments": type_of_dwelling_pop["condominiums_and_other_apartments"],
                "Landed": type_of_dwelling_pop["landed_properties"],
                "Others": type_of_dwelling_pop["others"]
            }

            out.append({
                "_id": rname,
                "data": new
            })

            # # no need to change
            # ethnic_group = rdata.get("Ethnic Group", None)
            # household_structure = rdata.get("Household Structure", None)
            # industry = rdata.get("Industry", None)
            # language_literate = rdata.get("Language Literate", None)
            # marital_status = rdata.get("Marital Status", None)
            # occupation = rdata.get("Occupation", None)
            # mode_of_transport_school = rdata.get("Mode Of Transport School", None)
            # religion = rdata.get("Religion", None)
            # spoken_at_home = rdata.get("Spoken At Home", None)
            # tenancy = rdata.get("Tenancy", None)
        
        except Exception as err:
            errors.append((rname, str(err)))
    
    print("\nERRORS:", errors)
        
    return out


