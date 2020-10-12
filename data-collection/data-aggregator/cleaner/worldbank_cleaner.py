def clean_worldbank(data):
    """
    converts values in time series data to floats
    """

    for cname, cdata in data.items():
        for fname, fdata in cdata.items():

            cdata[fname] = {year: float(value) for year, value in fdata.items()}
    
    return data