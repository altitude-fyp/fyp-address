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


def clean_charts(data_obj):
    """
    this function cleans onemap data for frontend
    """

    def clean_economic_status(data_obj):
        """
        this function cleans onemap the economic status 
        """
        data = {'Employed':0, 'Unemployed':0, 'Inactive':0}

        for key,value in data_obj.items():
            if 'employed' in key:
                data['Employed'] += value
            elif 'unemployed' in key:
                data['Unemployed'] += value
            elif 'inactive' in key:
                data['Inactive'] += value

        return {"labels":list(data.keys()), "data":list(data.values())}
        
    def clean_education_attending(data_obj):
        """
        this function cleans the education 
        """

        data = {'Pre Primary':0, 'Primary':0, 'Secondary':0, 'Post Secondary':0, 'Polytechnic':0, 'Professional Qualification Diploma':0, 'University':0}

        for key,value in data_obj.items():
            if 'pre_primary' in key:
                data['Pre Primary'] += value
            elif 'primary' in key:
                data['Primary'] += value
            elif 'secondary' in key:
                data['Secondary'] += value
            elif 'post_secondary' in key:
                data['Post Secondary'] += value
            elif 'polytechnic' in key:
                data['Polytechnic'] += value
            elif 'prof_qualification_diploma' in key:
                data['Professional Qualification Diploma'] += value
            elif 'university' in key:
                data['University'] += value

        return {"labels":list(data.keys()), "data":list(data.values())}
        
    def clean_ethnic_group(data_obj):
        """
        this function cleans the ethnic group 
        """

        data = {'Chinese':0, 'Malays':0, 'Indian':0, 'Others':0}

        for key,value in data_obj.items():
            if 'chinese' in key:
                data['chinese'] += value
            elif 'malays' in key:
                data['malays'] += value
            elif 'indian' in key:
                data['indian'] += value
            elif 'others' in key:
                data['others'] += value

        return {"labels":list(data.keys()), "data":list(data.values())}
        
    def clean_household_monthly_income(data_obj):
        """ 
        this function cleans the household monthly income 
        """

        data = {'Below 1000':0, '1000 to 1999':0, '2000 to 2999':0, '3000 to 3999':0, '4000 to 4999':0, 
                '5000 to 5999':0, '6000 to 6999':0, '7000 to 7999':0, '8000 to 8999':0, '9000 to 9999':0, 
                '10000 or more':0}

        for key,value in data_obj.items():

            if 'below' in key and '1000' in key:
                data['Below 1000'] += value
            elif '1000' in key and '1999' in key:
                data['1000 to 1999'] += value
            elif '2000' in key and '2999' in key:
                data['2000 to 2999'] += value
            elif '3000' in key and '3999' in key:
                data['3000 to 3999'] += value
            elif '4000' in key and '4999' in key:
                data['4000 to 4999'] += value
            elif '5000' in key and '5999' in key:
                data['5000 to 5999'] += value
            elif '6000' in key and '6999' in key:
                data['6000 to 6999'] += value
            elif '7000' in key and '7999' in key:
                data['7000 to 7999'] += value
            elif '8000' in key and '8999' in key:
                data['8000 to 8999'] += value
            elif '9000' in key and '9999' in key:
                data['9000 to 9999'] += value
            elif 'sgd' in key:
                data['10000 or more'] += value

        return {"labels":list(data.keys()), "data":list(data.values())}
        
    def clean_household_size(data_obj):
        """ 
        this function cleans the household size 
        """

        data = {}

        for key,value in data_obj.items():
            if str(value) != '' and 'person' in key:
                data[key.replace('person','')] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_household_structure(data_obj):
        """ 
        this function cleans the household structure 
        """

        pass

    def clean_income_from_work(data_obj):
        """ 
        this function cleans the income from work
        """

        data = {'Below 1000':0, '1000 to 1999':0, '2000 to 2999':0, '3000 to 3999':0, '4000 to 4999':0, 
                    '5000 to 5999':0, '6000 to 6999':0, '7000 to 7999':0, '8000 or more':0}

        for key,value in data_obj.items():
            
            if 'below' in key and '1000' in key:
                data['Below 1000'] += value
            elif '1000' in key and '1999' in key:
                data['1000 to 1999'] += value
            elif '2000' in key and '2999' in key:
                data['2000 to 2999'] += value
            elif '3000' in key and '3999' in key:
                data['3000 to 3999'] += value
            elif '4000' in key and '4999' in key:
                data['4000 to 4999'] += value
            elif '5000' in key and '5999' in key:
                data['5000 to 5999'] += value
            elif '6000' in key and '6999' in key:
                data['6000 to 6999'] += value
            elif '7000' in key and '7999' in key:
                data['7000 to 7999'] += value
            elif '8000' in key:
                data['8000 or more'] += value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_industry(data_obj):
        """ 
        this function cleans the industry
        """

        remove = ['planning_area', 'year']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').capitalise()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_language_literature(data_obj):
        """ 
        this function cleans the language literature
        """

        pass

    def clean_marital_status(data_obj):
        """ 
        this function cleans the marital status
        """
        data = {}

        for key, value in data_obj.items():
            industry_name = key.replace('_', ' ').capitalise()
            data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_mode_of_transport_school(data_obj):

        remove = ['planning_area', 'year']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').capitalise()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_occupation(data_obj):
        """ 
        this function cleans the occupation
        """

        remove = ['planning_area', 'year']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').capitalise()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_population_age_group(data_obj):
        pass
    def clean_religion(data_obj):
        """ 
        this function cleans the religion
        """
        remove = ['planning_area', 'year']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').capitalise()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_spoken_at_home(data_obj):
        """ 
        this function cleans the spoken at home
        """
        remove = ['planning_area', 'year']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').capitalise()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_tenancy(data_obj):
        """ 
        this function cleans the tenancy
        """
        remove = ['planning_area', 'year']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').capitalise()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_type_of_dwelling_household(data_obj):
        """ 
        this function cleans the dwelling household
        """
        remove = ['planning_area', 'year', 'total_hdb']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').capitalise()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_type_of_dwelling_pop(data_obj):
        """ 
        this function cleans the dwelling household
        """
        remove = ['planning_area', 'year', 'total_hdb', 'total']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').capitalise()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}
