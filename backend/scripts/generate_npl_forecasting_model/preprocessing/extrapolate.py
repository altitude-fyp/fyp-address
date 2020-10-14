def extrapolate(data, desired=[i for i in range(2000,2020)], restrict=False):
    """
    input: time series data with missing years
    
        eg. {2005: 123, 2006:124, 2009: 345, 2010: 567, ... 2017:900}

    output: autofilled time series data from years 2000-2019

        eg. {2000: _, 2001: _, ... 2019: _}

    """

    def fillmid(data):
        """
        input: sorted list of tuples (year, value)
        output: fills missing years in the middle
        """

        data = {int(k): float(v) for k,v in data.items()}

        lis = [(year,val) for year,val in data.items()]
        lis.sort(key=lambda x:x[0])

        gaps = []

        for i in range(len(lis)-1):

            left, _ = lis[i]

            right, __ = lis[i+1]

            if right - left == 1:
                continue

            gaps.append({
                "left": left,
                "right": right,
                "years": [i for i in range(left+1, right)]
            })

        for gap in gaps:
            left = data[gap["left"]]
            right = data[gap["right"]]

            step = (right - left) / (len(gap["years"])+1)

            current = left
            for year in gap["years"]:
                current += step
                data[year] = current

        return [(k,v) for k,v in sorted(data.items(), key=lambda x:x[0])]

    data = fillmid(data)
    
    increases = []
    for i in range(len(data)-1):
        _, val = data[i]
        __, nextval = data[i+1]
        
        increases.append(nextval-val)
        
    avg = sum(increases)/len(increases)
    if avg > 0:
        avg = avg ** 0.5
    else:
        avg = -1 * abs(avg)**0.5
    
    minyear, minyearval = data[0]
    maxyear, maxyearval = data[-1]
    
    left = list(range(min(desired), minyear))[::-1]
    right = list(range(maxyear+1, max(desired)+1))
    
    
    for l in left:
        minyearval -= avg
        data = [(l,minyearval)] + data
    
    for r in right:
        maxyearval += avg
        data.append((r,maxyearval))
    
    out = {k:v for k,v in data}
    
    def restrict_val(val):
        if val <= 0:
            return 0
        elif val >= 100:
            return 100
        return val
    
    return {k:restrict_val(v) for k,v in out.items()} if restrict else out