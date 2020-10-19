
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
                data['Chinese'] += value
            elif 'malays' in key:
                data['Malays'] += value
            elif 'indian' in key:
                data['Indian'] += value
            elif 'others' in key:
                data['Others'] += value

        return {"labels":list(data.keys()), "data":list(data.values())}
        
    def clean_household_monthly_income(data_obj):
        """ 
        this function cleans the household monthly income 
        """

        data = {'Below 1000':0, '1000 to 1999':0, '2000 to 2999':0, '3000 to 3999':0, '4000 to 4999':0, 
                '5000 to 5999':0, '6000 to 6999':0, '7000 to 7999':0, '8000 to 8999':0, '9000 to 9999':0, 
                '10000 or more':0}

        for key,value in data_obj.items():

            if value:
                if 'below' in key and '1000' in key :
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
            if value:
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
                industry_name = key.replace('_', ' ').title()
                print(industry_name)
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_language_literature(data_obj):
        """ 
        this function cleans the language literature
        """
        data = {}

        for key, value in data_obj.items():
            if 'l2' in key and 'chi' in key:
                data['Chinese'] = value
            if 'l2' in key and 'mal' in key:
                data['Malay'] = value
            if 'l2' in key and 'tam' in key:
                data['Tamil'] = value
            if 'l2' in key and 'two' in key:
                data['Others'] = value
        
        return {"labels":list(data.keys()), "data":list(data.values())}


    def clean_marital_status(data_obj):
        """ 
        this function cleans the marital status
        """
        data = {}

        for key, value in data_obj.items():
            industry_name = key.replace('_', ' ').title()
            data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_mode_of_transport_school(data_obj):

        remove = ['planning_area', 'year']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').title()
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
                industry_name = key.replace('_', ' ').title()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_population_age_group(data_obj):
        
        data = {}

        for key, value in data_obj.items():
            if 'total_total' != key and 'total' in key:
                try:
                    data[key.split('_')[1] + '-' + key.split('_')[2]] = value
                except:
                    pass
        
        return {"labels":list(data.keys()), "data":list(data.values())}

    def clean_religion(data_obj):
        """ 
        this function cleans the religion
        """
        remove = ['planning_area', 'year']

        data = {}

        for key, value in data_obj.items():
            if key not in remove:
                industry_name = key.replace('_', ' ').title()
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
                industry_name = key.replace('_', ' ').title()
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
                industry_name = key.replace('_', ' ').title()
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
                industry_name = key.replace('_', ' ').title()
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
                industry_name = key.replace('_', ' ').title()
                data[industry_name] = value

        return {"labels":list(data.keys()), "data":list(data.values())}


    cleaned_data = []

    d = {
        "Economic Status": clean_economic_status,
        "Education Attending": clean_education_attending,
        "Ethnic Group": clean_ethnic_group,
        "Household Monthly Income Work": clean_household_monthly_income,
        "Household Size": clean_household_structure,
        "Income From Work": clean_income_from_work,
        "Industry": clean_industry,
        "Language Literate": clean_language_literature,
        "marital Status": clean_marital_status,
        "Mode of Transport School": clean_mode_of_transport_school,
        "Occupation": clean_occupation,
        "Population Age Group": clean_population_age_group,
        "Religion": clean_religion,
        "Spoken At Home": clean_spoken_at_home,
        "Tenancy": clean_tenancy,
        "Type of Dwellin Household": clean_type_of_dwelling_household,
        "Type of Dwelling Pop": clean_type_of_dwelling_pop

    }

    for region in data_obj:
        clean_obj = {'_id': region['_id']}
        for indicator, indicator_object in region['data'].items():
            clean_func = d.get(indicator, None)

            if clean_func and indicator_object:
                clean_obj[indicator] = clean_func(indicator_object)

        cleaned_data.append(clean_obj)

    return cleaned_data