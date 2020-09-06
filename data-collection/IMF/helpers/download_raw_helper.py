"""
helper function for imf/download-raw.py
"""
import requests
import time
import pandas as pd 

def get_dataflow_mapping():
    print('Getting all parameters...')
#     To query all Dataflows
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    key = 'Dataflow'

    data = requests.get(f'{url}{key}').json()

    dataflows = data['Structure']['Dataflows']['Dataflow'] #Gather dataflows
    
    dataflow_ids = ['APDREO', 'BOP', 'BOPAGG', 'DOT', 'CPI', 'FAS', 'FDI', 'FSI']
    
    dataflow_id_names = {}
    
    for dataflow in dataflows:
        dataflow_name = dataflow['Name']['#text'] # Name of dataflow
        dataflow_id = dataflow['@id'].replace('DS-','') 
        if dataflow_id in dataflow_ids:
            dataflow_id_names[dataflow_id] = dataflow_name
    
    return dataflow_id_names

def get_data(country):
    print('Pulling',country + '...')
#     To query all Dataflows
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    key = 'Dataflow'

    try:
        data = requests.get(f'{url}{key}').json()
        dataflows = data['Structure']['Dataflows']['Dataflow'] #Gather dataflows
    except:
        pass

    dataflow_ids = ['APDREO', 'BOP', 'BOPAGG', 'DOT', 'CPI', 'FAS', 'FDI', 'FSI']

    dataflow_id_names = {}

    for dataflow in dataflows:
        dataflow_name = dataflow['Name']['#text'] # Name of dataflow
        dataflow_id = dataflow['@id'].replace('DS-','') 
        if dataflow_id in dataflow_ids:
            dataflow_id_names[dataflow_id] = dataflow_name

    all_data = {}
    
    for dataflow_id in dataflow_ids:

        columns = ['Geographical Areas', 'Indicator']

        url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
        key = 'DataStructure/' + dataflow_id

        try:
            codelists_data = requests.get(f'{url}{key}').json()['Structure']['CodeLists']['CodeList']

            all_codelists = {'dataflow_id': dataflow_id}

            country_details = {}

            for codelist in codelists_data:
                category = codelist['Name']['#text']

                if category in columns:

                    all_codelists[category] = []
                    codes = codelist['Code']

                    if type(codes) is dict:

                        if category == 'Indicator':
                            all_codelists[category].append(codes)
                        else:
                            all_codelists[category].append(codes)
                    else:

                        for code in codes:
                            if category == 'Indicator':
                                all_codelists[category].append(code)
                            else:
                                all_codelists[category].append(code)

            print('Running ' + dataflow_id_names[dataflow_id] + '...')
            all_data[dataflow_id_names[dataflow_id]] = all_codelists 
        except:
            pass

        df = pd.DataFrame(all_data)
        df = df.transpose()
        df = df.reset_index()

#     to mongoDB

#     get dataflow_id
    dataflow_ids = df['dataflow_id']
    countries_ids = df['Geographical Areas']

    all_country = {}

    all_indicators = {}
    indicator_descriptions = df['Indicator']
    
    for countryx in indicator_descriptions:
        for indicator in countryx:
            all_indicators[indicator['@value']] = indicator['Description']['#text']

    for index in range(len(dataflow_ids)):
        
        dataflow_id = dataflow_ids[index]
        countries = countries_ids[index]
        country_code = ''
        for countryc in countries:
            if country == countryc['Description']['#text']:
                country_code = countryc['@value']
        url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/'
        key = dataflow_id +'/A.'+ country_code +'.'
        try:
            data = (requests.get(f'{url}{key}').json()['CompactData']['DataSet']['Series'])
            all_country[dataflow_id_names[dataflow_id]] = data
        except:
            pass

    return all_country

def get_common_data():
    print('Getting all parameters...')
#     To query all Dataflows
    url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
    key = 'Dataflow'

    data = requests.get(f'{url}{key}').json()

    dataflows = data['Structure']['Dataflows']['Dataflow'] #Gather dataflows
    
    dataflow_ids = ['FSI']
    
    dataflow_id_names = {}
    
    for dataflow in dataflows:
        dataflow_name = dataflow['Name']['#text'] # Name of dataflow
        dataflow_id = dataflow['@id'].replace('DS-','') 
        if dataflow_id in dataflow_ids:
            dataflow_id_names[dataflow_id] = dataflow_name
            
    all_data = {}

    for dataflow_id in dataflow_ids:

        columns = ['Geographical Areas', 'Indicator']

        
        url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
        key = 'DataStructure/' + dataflow_id

        try:
            codelists_data = requests.get(f'{url}{key}').json()['Structure']['CodeLists']['CodeList']
            
            all_codelists = {'dataflow_id': dataflow_id}

            for codelist in codelists_data:
                category = codelist['Name']['#text']

                if category in columns:

                    all_codelists[category] = []
                    codes = codelist['Code']

                    if type(codes) is dict:
                        if category == 'Indicator':
                            all_codelists[category].append(codes)
                        else:
                            all_codelists[category].append(codes)
                    else:
                        
                        for code in codes:
                            if category == 'Indicator':
                                all_codelists[category].append(code)
                            else:
                                all_codelists[category].append(code)
            print('Running ' + dataflow_id + '...')
            all_data[dataflow_id_names[dataflow_id]] = all_codelists    
        
        except:
            del all_data[dataflow_id_names[dataflow_id]]

    df = pd.DataFrame(all_data)
    df = df.transpose()
    df = df.reset_index()
    
    return df

def get_batch_country_data(unique_countries):
    print('Getting all common countries data...')
    all_output = {}
    for country in unique_countries:
        all_output[country] = get_data(country)
        print(all_output[country].keys())
    return all_output

def get_indicator_mapping(dataflow_mapping, df):
    print('Getting all indicator names...')
    indicator_mapping = {}
    indicator_descriptions = df['Indicator']
    indicator_dataflow = df['dataflow_id']
    for index in range(len(indicator_descriptions)):
        indicator_mapping[dataflow_mapping[indicator_dataflow[index]]] = {}
        for indicator in indicator_descriptions[index]:
            indicator_mapping[dataflow_mapping[indicator_dataflow[index]]][indicator['@value']] = indicator['Description']['#text']
                
    return indicator_mapping


def get_common_countries(all_data):
    print('Getting all common countries...')
    all_countries = all_data['Geographical Areas']
    all_dataflow_id = all_data['dataflow_id']
    common_countries = {}

    for entry,countries in all_countries.items():
        for country in countries:
            if country['Description']['#text'] not in common_countries:
                common_countries[country['Description']['#text']] = 1
            else:
                common_countries[country['Description']['#text']] += 1

    unique_countries = []

    for key, value in common_countries.items():
        if value == 1:
            unique_countries.append(key)
    
    return unique_countries

def get_common_mapping(indicator_mapping, all_output):
    print('Getting all common indicators...')
    common_indicators = {}

    for country, data in all_output.items():
        for dataflow, indicators in data.items():
            
            if dataflow not in common_indicators:
                common_indicators[dataflow] = {}
                
            for indicator in indicators:
                try:
                    indicator_name = indicator_mapping[dataflow][indicator['@INDICATOR']]
                    if indicator_name in common_indicators[dataflow]:
                        common_indicators[dataflow][indicator_name] += 1
                    else:
                        common_indicators[dataflow][indicator_name] = 1
                except:
                    pass
                
    unique_indicators = {}
    
    for dataflow, indicators in common_indicators.items():
        print('Processing ' + dataflow + '...')
        all_countries = []
        if dataflow not in unique_indicators:
            unique_indicators[dataflow] = []
        

        for indicator, indicator_count in indicators.items():
            if indicator_count > 3  and indicator not in all_countries:
                all_countries.append(indicator)
        
        unique_indicators[dataflow] = all_countries
        
    return unique_indicators

def convert_all_country_data(indicator_mapping, all_country_data):
    print('Converting all common countries data...')
    converted_all_country_data = {}

    for country,dataflows in all_country_data.items():
        converted_all_country_data[country] = {}
        for dataflow, indicators in dataflows.items():
            converted_all_country_data[country][dataflow] = {}
            for indicator in indicators:
                converted_all_country_data[country][dataflow][indicator_mapping[dataflow][indicator['@INDICATOR']]] = indicator['Obs']
    
    return converted_all_country_data

def get_npl_countries(common_data):

    must_indicators = {}

    #only non-performing loans by percent
    for country_indicators in common_data['Indicator']:
        for indicator in country_indicators:
            description = indicator['Description']['#text'].lower()
            if 'non-performing loans' in description and 'percent' in description:
                must_indicators[indicator['@value']] = indicator['Description']['#text']

    fsi_countries = {}           

    for countries in common_data['Geographical Areas']:
        for country_description in countries:
            fsi_countries[country_description['Description']['#text']] = {}
            print(country_description['Description']['#text'])
            for indicator in must_indicators:
                url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/'
                key = 'FSI' +'/A.'+ country_description['@value'] +'.' + indicator + '.'
#                 print(must_indicators[indicator])
                try:
                    data = (requests.get(f'{url}{key}').json()['CompactData']['DataSet']['Series'])
                    fsi_countries[country_description['Description']['#text']][must_indicators[indicator]] = data
                except:
                    pass
    
    finalised_countries = {}
    
    for country in fsi_countries:
        if (len(fsi_countries[country])) >= 2:
            finalised_countries[country] = fsi_countries[country]

    return finalised_countries.keys()