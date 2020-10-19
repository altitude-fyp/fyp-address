"""
cleans onemap data and removes null values
"""
def clean(o):
    
    def sieve(feature_object):            
        """
        remove entries with no data
        """
            
        out = []

        for year, yo in feature_object.items():
            
            if type(yo) == dict and yo.get("Result", None) == "No Data Available!":
                continue
            
            else:    
                out.append((year, yo))
        
        return out if len(out) else None
                
    report = {"2000":0, "2010":0, "2015":0}
    
    for ao in o:
        data = ao["data"]
        
        for fname, fo in data.items():
                        
            fo = sieve(fo)
            
            if fo:
                fo = max(fo, key=lambda x:x[0])
                report[fo[0]] += 1
                fo = fo[-1]
                    
                data[fname] = combine(fo)
                
            else:
                data[fname] = None
                
    print("Updatedness report - key: year, value: no. of times year is used -", report, "\n")
        
    return o


def combine(fo):
    """
    as of now, fo is a list of objects
    this function combines the objects into 1 dictionary
    """

    if len(fo) == 1:
        return fo[0]

    else:
        whitelist = ["planning_area", "year", "gender"]

        out = {}
        for o in fo:
            if "gender" in o:
                for k,v in o.items():
                    if k not in whitelist:
                        out[k + "_" + o["gender"].lower()] = v
            else:
                for k,v in o.items():
                    out[k] = v
        
        return out