"""
contains combine_as_api_data, which combines all 3 data sources
    - output is meant for frontend to call 
    - human readability takes precedence over machine readability here
"""

def combine_as_api_data(countries, wikipedia, imf):
    return {}