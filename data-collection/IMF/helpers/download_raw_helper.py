"""
helper function for imf/download-raw.py
"""
import requests
import time
import pandas as pd 

def get_dataflow_parameters():
    columns = ['Geographical Areas', 'Indicator']
    dataflow_ids = ['APDREO', 'CPI', 'FAS', 'FDI', 'FSI']
    all_data = {'Geographical Areas':[],'Indicator':[]}
    for dataflow_id in dataflow_ids:

        url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
        key = 'DataStructure/' + dataflow_id

        codelists_data = requests.get(f'{url}{key}').json()['Structure']['CodeLists']['CodeList']
        country_details = {}
        for codelist in codelists_data:
            category = codelist['Name']['#text']
            if category in columns:
                codes = codelist['Code']
                for code in codes:
                    all_data[category].extend([code]) 

    unique_country_mapping = list({v['@value']:v for v in all_data['Geographical Areas']}.values())
    unique_indicator_mapping = list({v['@value']:v for v in all_data['Indicator']}.values())
    
    return {'Geographical Areas': unique_country_mapping, 'Indicator': unique_indicator_mapping}

def dictionary_mapping(all_mapping):
    all_id_names = {'Geographical Areas': {}, 'Indicator': {}}
    for country in all_mapping['Geographical Areas']:
        all_id_names['Geographical Areas'][country['@value']] = country['Description']['#text']
    for indicator in all_mapping['Indicator']:
        all_id_names['Indicator'][indicator['@value']] = indicator['Description']['#text']
    return all_id_names

def get_npl_countries():
    columns = ['Geographical Areas', 'Indicator']
    dataflow_ids = ['FSI']
    all_data = {'Geographical Areas':[],'Indicator':[]}
    for dataflow_id in dataflow_ids:

        url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
        key = 'DataStructure/' + dataflow_id

        codelists_data = requests.get(f'{url}{key}').json()['Structure']['CodeLists']['CodeList']
        country_details = {}
        for codelist in codelists_data:
            category = codelist['Name']['#text']
            if category in columns:
                codes = codelist['Code']
                for code in codes:
                    all_data[category].extend([code])

    unique_country_mapping = list({v['@value']:v for v in all_data['Geographical Areas']}.values())
    unique_indicator_mapping = list({v['@value']:v for v in all_data['Indicator']}.values())

    must_indicators = {}
    #only non-performing loans by percent
    for country_indicators in unique_indicator_mapping:
        description = country_indicators['Description']['#text'].lower()
        if 'non-performing loans' in description and 'percent' in description:
            must_indicators[country_indicators['@value']] = country_indicators['Description']['#text']
    
    fsi_countries = {}
    
    for country_indicators in unique_country_mapping:
        fsi_countries[country_indicators['@value']] = {}
        print(country_indicators['Description']['#text'])
        for indicator in must_indicators:
            url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/'
            key = 'FSI' +'/Q.'+ country_indicators['@value'] +'.' + indicator + '.'
            try:
                data = requests.get(f'{url}{key}').json()['CompactData']['DataSet']['Series']['Obs']
                #check empty
                empty = False
                cleaned_data = {}
                for entry in data:
                    time_period_value = entry["@TIME_PERIOD"]
                    obs_value = entry["@OBS_VALUE"]
                    cleaned_data[time_period_value] = float(obs_value)
                    if obs_value == 0 or obs_value == None:
                        empty = True
                if empty == False:
                    print(cleaned_data)
                    fsi_countries[country_indicators['@value']][must_indicators[indicator]] = cleaned_data
            except:
                pass
    
    finalised_countries = []
    
    for country in fsi_countries:
        if (len(fsi_countries[country])) >= 2:
            finalised_countries.append(country)

    return finalised_countries

chosen_indicators = {'APDREO':['LUR','PCPI_PCH','PCPIE_PCH','NGDP_R_PPP_PC_PCH'],
                     'CPI':['PCPI_IX'], 
     'FAS':['FCIODD_NUM','FCIOFI_NUM','FCIODU_NUM','FCIODMF_NUM','FCNODC_NUM','FCRODC_PE_NUM' ,'FCRODU_PE_NUM',
            'FCSODCG_GDP_PT' ,'FCBODC_NUM'], 
     'FDI':['FD_FD_IX', 'FD_FIA_IX', 'FD_FID_IX', 'FD_FIE_IX', 'FD_FI_IX','FD_FMA_IX' ,'FD_FMD_IX','FD_FME_IX', 
            'FD_FM_IX'], 'FSI': ['FSANL_PT', 'FSKNL_PT', 'FSBPNL_PT']}

def get_data(chosen_indicators, period, npl_countries):
    all_country = {}
    for country_code in npl_countries:
        all_country[country_code] = {}
        for dataflow_id, indicators in chosen_indicators.items():
            for indicator in indicators:
                url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/CompactData/'
                key = dataflow_id +'/' + period + '.' + country_code +'.' + indicator
                try:
                    data = requests.get(f'{url}{key}').json()['CompactData']['DataSet']['Series']['Obs']
                    #check empty
                    cleaned_data = {}
                    empty = False
                    for entry in data:
                        time_period_value = entry['@TIME_PERIOD']
                        obs_value = entry["@OBS_VALUE"]
                        if time_period_value > 2000:
                            cleaned_data[time_period_value] = float(obs_value)
                        if obs_value == 0 or obs_value == None:
                            empty = True
                    if empty == False:
                        all_country[country_code][indicator] = cleaned_data
                        print(country_code, indicator, cleaned_data.keys())
                except:
                    pass
                
    return all_country

def convert_dictionary(all_data, all_mapping):
    converted = {}
    for country, indicators in all_data.items():
        converted[all_mapping['Geographical Areas'][country]] = {}
        for indicator, data in indicators.items():
            converted[all_mapping['Geographical Areas'][country]][all_mapping['Indicator'][indicator]] = data  
    return converted