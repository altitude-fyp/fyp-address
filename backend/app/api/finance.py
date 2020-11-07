from app import app
import pandas as pd 
import ast

@app.get("/api/finance/{regions}")
def get_individual_address_data(regions):
    # Load generated finance csv
    df = pd.read_csv("scripts/generate_finance/finance.csv")
    # Set region column to be index
    df.set_index("region", inplace = True)
    
    result = {"status": "success", "data" : {}}

    region_list = regions.split(",")
    # Get product list
    products = [ { "region": region, "products": [ast.literal_eval(df.loc[region, 'citi_products'])] } for region in region_list ]
    # Get graph 1
    products = [ { "region": region, "products": [ast.literal_eval(df.loc[region, 'citi_products'])] } for region in region_list ]

    graph1 = {
        "title": "Indifference curve",
        "regions": [region for region in region_list],
        "x-axis": ast.literal_eval(df.loc[region_list[0], 'graph_1_x']),
        "y-axis": [ast.literal_eval(df.loc[region, 'graph_1_y']) for region in region_list]
    }

    graph2 = {
        "title": "Utility as a Function of Allocation to the Risky Asset",
        "regions": [region for region in region_list],
        "x-axis": ast.literal_eval(df.loc[region_list[0], 'graph_2_x']),
        "y-axis": [ast.literal_eval(df.loc[region, 'graph_2_y']) for region in region_list]
    }

    result["data"]["products"] = products
    result["data"]["graph_1"] = graph1
    result["data"]["graph_2"] = graph2

    return result

