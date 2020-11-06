from app import app
from mongodb_helper import *
from collections import defaultdict
from pydantic import BaseModel
import json
from typing import Optional


class Item(BaseModel):
    economic_status : Optional[str]
    household_monthly_income_work : Optional[str]
    income_from_work : Optional[str]
    population_age_group: Optional[str]

@app.post("/api/analytics/market_segment/")
def get_market_segment(item:Item):
    """
    input: takes in a dictionary of chosen features and respective categories
    output: top 5 regions with selected market segments
    """
    chosen_categories = {}
    if item.economic_status:
        chosen_categories['Economic Status'] = item.economic_status
    if item.household_monthly_income_work:
        chosen_categories['Household Monthly Income Work'] = item.household_monthly_income_work
    if item.income_from_work:
        chosen_categories['Income From Work'] = item.income_from_work
    if item.population_age_group:
        chosen_categories['Population Age Group'] = item.population_age_group

    db = get_database()

    combined_features = {}
    raw_features = {}

    for region in db["onemap.summary"].find():

        for feature, categories in region["data"].items():
            total = sum(categories.values())

            if feature not in combined_features:
                combined_features[feature] = {}

            for category, value in categories.items():

                if category not in combined_features[feature]:
                    combined_features[feature][category] = {}
                    raw_features[category] = {}

                try:
                    combined_features[feature][category][region["_id"]] = value/total * 100
                    raw_features[category][region["_id"]] = value/total * 100
                except:
                    pass
    
    for feature,categories in combined_features.items():
        for category in categories:
            combined_features[feature][category] = list(dict(sorted(combined_features[feature][category].items(), key=lambda kv: kv[1], reverse = True)).keys())

    final_ranking = defaultdict(lambda: 0)

    for chosen_category in chosen_categories:
        regions = combined_features[chosen_category][chosen_categories[chosen_category]]
        
        for region in regions:
            final_ranking[region] += regions.index(region)

    final_ranking = list(dict(sorted(final_ranking.items(), key=lambda kv: kv[1])[1:10]).keys())
    
    final_output = []

    for region in final_ranking:
        region_output = {}
        region_output['name'] = region
        region_output['value'] = []
        for chosen_category in chosen_categories:
            try: region_output['value'].append({'name': chosen_category + ' - ' + chosen_categories[chosen_category], 'value': round(raw_features[chosen_categories[chosen_category]][region],2)})
            except: pass
        final_output.append(region_output)

    try:
        return {
            "status": "success",
            "regions": final_output
        }
    
    except Exception as err:
        return {
            "status": "failure",
            "error": str(err),
        }