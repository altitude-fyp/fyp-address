from app import app
from .analytics_helper.property_category import *
from .api_helper.common import *
from pydantic import BaseModel
from .countries import *
from .regions import *
from .analytics import *
from .npl import *
from .charts import *
from .onemap_region_summary import *
from typing import List
import pickle

class Item(BaseModel):
    address: str

class Addresses(BaseModel):
    # addresses: List[ItemList]
    addresses: list = [[]]

COUNTRIES = pickle.load(open("pickled/constants.sav", "rb"))

@app.post("/api/address")
def get_individual_address_data(item:Item):
    """
    Main API to receive an address input and do the following:
    1. Verify whether it is a valid address
    2. Find out what type of property
    3. Find which region does the address belong to
    4. Return region data
    5. Return country data (at the moment, Singapore)
    """
    address = item.address

    # If users input a country name, 
    if address in [*COUNTRIES]:
        country_data = get_country_statistics_(address)[address]
        return {"status": "success", "data": {"country": address, "country_data": country_data}}
    else:
        country_data = get_country_statistics_("Singapore")["Singapore"]
        country = "Singapore"

    # Call Onemap API to get detailed address
    onemap_result = search_onemap_api(address)

    # Validation
    if onemap_result["found"] == 0:
        return {"status": "error", "data": "Address is invalid. Please enter another address."}
    
    elif onemap_result["found"] != 1:
        return {"status": "error", "data": "Too many similar addresses found. Please enter a more specific address."}

    result = {"status": "success", "data": {}}

    onemap_address = onemap_result["results"][0]

    region_onemap = get_planning_area_onemap(onemap_address["LATITUDE"], onemap_address["LONGITUDE"])
    region_name = region_onemap[0]["pln_area_n"]
    region_data = get_regions_data(region_name)["data"]

    # Find out property type
    property_type = check_property_type(onemap_address)

    return {
        "status": "success",
        "data": {
            "summary": {
                "property_type": property_type,
                "region_found": region_name,
                "country_found": country,
            },
            "analytics_result": {
                "top_3_similar_countries": { country: get_top_countries_for_api(country) },
                "npl_features": { country: get_sorted_npl_data_by_country(country)[country] }
            },
            "npl_analytics": {
                "npl_forecast": get_npl_forecast(),
                "npl_charts": get_sorted_npl_data_for_api(),
                "npl_graph": { country: get_chart_data_for_api(country) }
            },   
            "region_data": region_data,
            "region_summary_data": { region_name: onemap_region_summary_by_region(region_name.lower())["data"] }, 
            "country_data": country_data,
            "country_chart_data" : { country: get_country_chart_data_for_api(country) }   
        }
    }

@app.post("/api/address/frontend")
def get_individual_address_data_for_frontend(item:Item):
    """
    Main API to receive an address input and do the following:
    1. Verify whether it is a valid address
    2. Find out what type of property
    3. Find which region does the address belong to
    4. Return region data
    5. Return country data (at the moment, Singapore)
    """
    address = item.address
    # Call Onemap API to get detailed address
    onemap_result = search_onemap_api(address)

    # Validation
    if onemap_result["found"] == 0:
        return {"status": "error", "data": "Address is invalid. Please enter another address."}
    
    elif onemap_result["found"] != 1:
        return {"status": "error", "data": "Too many similar addresses found. Please enter a more specific address."}

    result = {"status": "success", "data": {}}

    onemap_address = onemap_result["results"][0]

    region_onemap = get_planning_area_onemap(onemap_address["LATITUDE"], onemap_address["LONGITUDE"])
    region_name = region_onemap[0]["pln_area_n"]

    # Find out property type
    property_type = check_property_type(onemap_address)

    return {
        "status": "success",
        "data": {
            "property_type": property_type,
            "region_found": region_name,
            "country_found": "Singapore"
        }
    }

@app.post("/api/address/csv")
def get_address_csv_data(item:Addresses):
    addresses = item.addresses

    # addresses = [
    #     ["SINGAPORE", "380105"],
    #     ["SINGAPORE", "534051"]
    # ]

    # Property type
    property_type_list = []

    # Region  
    postal_code_list = []

    # Count
    country_list = {}
    region_list = {}

    # Final result data
    country_data = {}
    region_data = {}

    # Fail records
    fail_data = []

    # Analytics result

    for address in addresses:
        isAddressFound = True

        country = address["addr_cntry_txt"].title()
        postal_code = address["addr_postal_cde"]

        if country not in country_data:
            country_list[country] = 1
            # Get country data
            country_data[country] = get_country_statistics_(country)[country]
        else:
            country_list[country] += 1

        if postal_code not in postal_code_list:
            postal_code_list.append(postal_code)

            # Call Onemap API to get detailed address
            onemap_result = search_onemap_api(postal_code)

            if onemap_result["found"] == 0:
                fail_data.append(address)
                isAddressFound = False

            elif onemap_result["found"] >= 1:
                onemap_address = onemap_result["results"][0] 

            if isAddressFound:
                region_onemap = get_planning_area_onemap(onemap_address["LATITUDE"], onemap_address["LONGITUDE"])

                region_name = region_onemap[0]["pln_area_n"]
                if region_name not in region_data:
                    region_list[region_name] = 1
                    region_data[region_name.title()] = get_regions_data(region_name)["data"]
                else:
                    region_list[region_name] += 1

                # Find out property type
                property_type = check_property_type(onemap_address)

                if property_type not in property_type_list:
                    property_type_list.append(property_type)

    return {
        "status": "success",
        "data": {  
            "summary": {
                "valid": {
                    "total": len(addresses) - len(fail_data),
                    "housing_type": property_type,
                    "region_found": region_list,
                    "country_found": country_list,
                },
                "invalid": {
                    "total": len(fail_data),
                    "invalid_data": fail_data,
                },
            },
            "analytics_result": {
                "top_3_similar_countries": { country: get_top_countries_for_api(country) for country in country_data },
                "npl_features": { country: get_sorted_npl_data_by_country(country)[country] for country in country_data }
            },
            "npl_analytics": {
                "npl_forecast": get_npl_forecast(),
                "npl_charts": get_sorted_npl_data_for_api(),
                "npl_graph": { country: get_chart_data_for_api(country) for country in country_data }
            },   
            "region_data": region_data,
            "region_summary_data": { region: onemap_region_summary_by_region(region.lower())["data"] for region in region_data }, 
            "country_data": country_data,
            "country_chart_data" : { country: get_country_chart_data_for_api(country) for country in country_data }       
        }
    }

@app.post("/api/address/frontend/csv")
def get_address_csv_data(item:Addresses):

#     item = {"addresses":[{"addr_cntry_txt":"SINGAPORE","addr_postal_cde":"529344","addr_line1_txt":"#01-05 Meadows","addr_line2_txt":"21 Tampines St 32","addr_line3_txt":"-"},
# {"addr_cntry_txt":"SINGAPORE","addr_postal_cde":"357707","addr_line1_txt":"#01-05 Meadows","addr_line2_txt":"21 Tampines St 32","addr_line3_txt":"-"},
# {"addr_cntry_txt":"SINGAPORE","addr_postal_cde":"357708","addr_line1_txt":"#01-05 Meadows","addr_line2_txt":"21 Tampines St 32","addr_line3_txt":"-"},
# {"addr_cntry_txt":"SINGAPORE","addr_postal_cde":"357709","addr_line1_txt":"#01-05 Meadows","addr_line2_txt":"21 Tampines St 32","addr_line3_txt":"-"},
# {"addr_cntry_txt":"SINGAPORE","addr_postal_cde":"357706","addr_line1_txt":"#01-05 Meadows","addr_line2_txt":"21 Tampines St 32","addr_line3_txt":"-"},
# {"addr_cntry_txt":"SINGAPORE","addr_postal_cde":"560101","addr_line1_txt":"#01-05 Meadows","addr_line2_txt":"21 Tampines St 32","addr_line3_txt":"-"},
# {"addr_cntry_txt":"SINGAPORE","addr_postal_cde":"560102","addr_line1_txt":"#01-05 Meadows","addr_line2_txt":"21 Tampines St 32","addr_line3_txt":"-"},
# {"addr_cntry_txt":"SINGAPORE","addr_postal_cde":"357705","addr_line1_txt":"221 Boon Lay Place","addr_line2_txt":"Block 221B #01-23","addr_line3_txt":"Jurong West"}]}
#     addresses = item["addresses"]

    addresses = item.addresses

    property_type_list = {"HDB": 0, "Private": 0, "Others": 0}

    # Region  
    postal_code_list = []

    # Count
    country_list = {}
    region_list = {}

    # Fail records
    fail_data = []

    # Analytics result

    for address in addresses:
        isAddressFound = True

        country = address["addr_cntry_txt"].title()
        postal_code = address["addr_postal_cde"]

        if country not in country_list:
            country_list[country] = 1
        else:
            country_list[country] += 1

        if postal_code not in postal_code_list:
            postal_code_list.append(postal_code)

            # Call Onemap API to get detailed address
            onemap_result = search_onemap_api(postal_code)

            if onemap_result["found"] == 0:
                fail_data.append(address)
                isAddressFound = False

            elif onemap_result["found"] >= 1:
                onemap_address = onemap_result["results"][0] 

            if isAddressFound:
                region_onemap = get_planning_area_onemap(onemap_address["LATITUDE"], onemap_address["LONGITUDE"])
                
                try:
                    region_name = region_onemap[0]["pln_area_n"]
                except:
                    return { "status": "error", "data": "Onemap Token has expired." }
                if region_name not in region_list:
                    region_list[region_name] = 1
                else:
                    region_list[region_name] += 1

                # Find out property type
                property_type = check_property_type(onemap_address)

                if property_type in property_type_list:
                    property_type_list[property_type] += 1

    return {
        "status": "success",
        "data": {
            "valid": {
                "total": len(addresses) - len(fail_data),
                "housing_type": property_type_list,
                "region_found": sort_dictionary(region_list),
                "country_found": sort_dictionary(country_list),
            },
            "invalid": {
                "total": len(fail_data),
                "invalid_data": fail_data,
            }    
        }
    }

def sort_dictionary(input_dict):
    return {k.title(): v for k, v in sorted(input_dict.items(), key=lambda item: item[1], reverse = True)}