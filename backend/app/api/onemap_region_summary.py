from app import app
from mongodb_helper import *

@app.get("/api/onemap_region_summary")
def onemap_region_summary():
    db = get_database()

    regions = [i for i in db["onemap.summary"].find()]
    out = []

    for region in regions:
        
        data = {}

        # EMPLOYMENT 
        try: 
            econ = region["data"]["Economic Status"]
            percentage_employed = round( econ["Employed"]*100 / sum(econ.values()), 1 )
            data["Employment"] = {"Percentage Employed": percentage_employed}
        except: 
            data["Employment"] = {}


        # Highest % of Household Monthly Income Work
        try:
            householdincome = region["data"]["Household Monthly Income Work"]
            total = sum(householdincome.values())
            
            hhisum = {}
            hhisum["Percentage Low Income [0-5000]"] = round(householdincome["Low [0-5000]"]*100 / total, 1)
            hhisum["Percentage Middle Income [5000-10000]"] = round(householdincome["Middle [5000-10000]"]*100 / total, 1)
            hhisum["Percentage High Income [10000+]"] = round(householdincome["High [10000+]"]*100 / total, 1)

        except:
            hhisum = {}

        data["Household Monthly Income Work"] = hhisum

        # Highest % of Income From Work 
        try: 
            income = region["data"]["Income From Work"]
            total = sum(income.values())

            isum = {}
            isum["Percentage Low Income [0-5000]"] = round(income["Low [0-3000]"]*100 / total, 1)
            isum["Percentage Middle Income [5000-10000]"] = round(income["Middle [3000-6000]"]*100 / total, 1)
            isum["Percentage High Income [10000+]"] = round(income["High [6000+]"]*100 / total, 1)

        except:
            isum = {}

        data["Income From Work"] = isum


        # Highest % of Population Age Group
        try:
            pag = region["data"]["Population Age Group"]
            total = sum(pag.values())

            psum = {}
            psum["Percentage 19 and below"] = round(pag["0-19"]*100 / total, 1)
            psum["Percentage 20-59"] = round((pag["20-39"] + pag["40-59"])*100/ total, 1)
            psum["Percentage 60 and above"] = round(pag["60+"]*100 / total, 1)

        except:
            psum = {}

        data["Population Age Group"] = psum

        out.append({
            "_id": region["_id"],
            "data": data
        })

    return out

@app.get("/api/onemap_region_summary/{region}")
def onemap_region_summary_by_region(region):
    db = get_database()

    region = db["onemap.summary"].find_one({"_id": region})
         
    data = {}

    # EMPLOYMENT 
    try: 
        econ = region["data"]["Economic Status"]
        percentage_employed = round( econ["Employed"]*100 / sum(econ.values()), 1 )
        data["Employment"] = {"Percentage Employed": percentage_employed}
    except: 
        data["Employment"] = {}


    # Highest % of Household Monthly Income Work
    try:
        householdincome = region["data"]["Household Monthly Income Work"]
        total = sum(householdincome.values())
        
        hhisum = {}
        hhisum["Percentage Low Income [0-5000]"] = round(householdincome["Low [0-5000]"]*100 / total, 1)
        hhisum["Percentage Middle Income [5000-10000]"] = round(householdincome["Middle [5000-10000]"]*100 / total, 1)
        hhisum["Percentage High Income [10000+]"] = round(householdincome["High [10000+]"]*100 / total, 1)

    except:
        hhisum = {}

    data["Household Monthly Income Work"] = hhisum

    # Highest % of Income From Work 
    try: 
        income = region["data"]["Income From Work"]
        total = sum(income.values())

        isum = {}
        isum["Percentage Low Income [0-5000]"] = round(income["Low [0-3000]"]*100 / total, 1)
        isum["Percentage Middle Income [5000-10000]"] = round(income["Middle [3000-6000]"]*100 / total, 1)
        isum["Percentage High Income [10000+]"] = round(income["High [6000+]"]*100 / total, 1)

    except:
        isum = {}

    data["Income From Work"] = isum


    # Highest % of Population Age Group
    try:
        pag = region["data"]["Population Age Group"]
        total = sum(pag.values())

        psum = {}
        psum["Percentage 19 and below"] = round(pag["0-19"]*100 / total, 1)
        psum["Percentage 20-59"] = round((pag["20-39"] + pag["40-59"])*100/ total, 1)
        psum["Percentage 60 and above"] = round(pag["60+"]*100 / total, 1)

    except:
        psum = {}

    data["Population Age Group"] = psum

    return {
        "status": "success",
        "data": data
    }