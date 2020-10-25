from app import app
from .analytics_helper.property_category import *
from .api_helper.common import *
from pydantic import BaseModel
from .countries import *
from .regions import *
import pickle

class Item(BaseModel):
    address: str

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

    onemap_address = onemap_result["results"][0]

    # Validation
    if onemap_result["found"] == 0:
        return {"status": "error", "data": "Address is invalid. Please enter another address."}

    elif onemap_result["found"] != 1:
        return {"status": "error", "data": "Too many similar addresses found. Please enter a more specific address."}

    result = {"status": "success", "data": {}}

    region_onemap = get_planning_area_onemap(onemap_address["LATITUDE"], onemap_address["LONGITUDE"])
    region_name = region_onemap[0]["pln_area_n"]
    region_data = get_regions_data(region_name)["data"]

    # Find out property type
    property_type = check_property_type(onemap_address)

    result["data"]["house_type"] = property_type
    result["data"]["region"] = region_name
    result["data"]["country"] = country
    result["data"]["onemap_address"] = onemap_address
    result["data"]["region_data"] = region_data
    result["data"]["country_data"] = country_data

    return result

@app.post("/api/address/csv")
def post_address_csv(item:Item):
    return item.address