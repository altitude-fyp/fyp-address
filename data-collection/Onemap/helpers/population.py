from helpers.common import *
from helpers.constants import *

def get_area_list():
    """
    returns list of planning areas in singapore
    """
    response = requests.get(PLANNING_AREA_URL, params={
        'token': os.getenv("ONEMAP_TOKEN"),
        'year': YEAR,
    })
    return [i["pln_area_n"].lower() for i in json.loads(response.content)]

def get_population_data(db_insert_function):
    """
    gets economic data about singaporeans, segregated by area eg. orchard, seragoon, aljunied etc
    """
    print()
    years = [str(i) for i in [2000,2010,2015]]
    area_list = get_area_list()

    out = {}
    errors = []
        
    for area in area_list:

        area_obj = {}

        for fname, fendpoint in POPULATION_ENDPOINTS.items():

            fobj = {}

            for year in years:

                print(f"Pulling {area} {fname} for {year}" + " "*40, end="\r")

                try:
                    data = get_data(fendpoint, area, year=year)

                except Exception as err:
                    errors.append((str(err), area, fname, year))

                fobj[year] = data

            area_obj[fname] = fobj

        db_insert_function(area, area_obj)
        
        out[area] = area_obj

    print("\n")

    print(errors)

    return out
