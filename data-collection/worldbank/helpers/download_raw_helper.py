import numpy as np
import requests
import matplotlib.pyplot as plt
import pandas as pd
import csv
import xlrd
import matplotlib.lines as mlines
import xlsxwriter
import matplotlib.transforms as mtransforms
import statsmodels.api as sm
from bs4 import BeautifulSoup
from xml.dom import minidom
import xml.etree.cElementTree as et
import dask.dataframe as dd

def create_dict(SeriesName, Country, Year, Value):
    SeriesName, Country, Year, Value = list(SeriesName), list(Country), list(Year), list(Value)
    all_data = {}
    for i in range(len(Country)):
        if Country[i] not in all_data:
            all_data[Country[i]] = {SeriesName[i]: {Year[i]: Value[i]}}
        elif SeriesName[i] not in all_data[Country[i]]:
            all_data[Country[i]][SeriesName[i]] = {Year[i]: Value[i]}
        else:
            all_data[Country[i]][SeriesName[i]][Year[i]] = Value[i]
    return all_data

def get_worldbank_data():
    #grab all indicators
    page = requests.get('https://data.worldbank.org/indicator/')
    soup = BeautifulSoup(page.content, 'html.parser')

    th_all = soup.find_all('a')
    all_indicators = {}
    for th in th_all:
        try:
            if '/indicator/' in th['href'] and 'view=chart' in th['href']:
                all_indicators[th['href'].replace('/indicator/','').replace('?view=chart','')] = th.get_text()
        except:
            pass

    indicators = {k: all_indicators[k] for k in list(all_indicators)[:]}

    df=[]

    for tag,description in indicators.items():
        print('Running ' + description + '...')
        Countryname = []
        SeriesCode = []
        Year = []
        Value = []
        wiki = 'http://api.worldbank.org/v2/countries/all/indicators/' + str(tag) + '/?format=xml&date=2000:2019&per_page=20000'
        r = requests.get(wiki, stream=True)
        root = et.fromstring(r.content)

        for child in root.iter("{http://www.worldbank.org}indicator"):
            SeriesCode.append(description)
        for child in root.iter("{http://www.worldbank.org}country"):
            Countryname.append(child.text)
        for child in root.iter("{http://www.worldbank.org}date"):
            Year.append(child.text)
        for child in root.iter("{http://www.worldbank.org}value"):
            Value.append((child.text))
        test_df = pd.DataFrame.from_dict({'SeriesName': SeriesCode,
                                          'Country': Countryname,
                                          'Year': Year,
                                          'Value': Value}, orient='index')
        test_df = test_df.transpose()
        df.append(test_df)

    df=pd.concat(df)

    data = pd.DataFrame(df.to_records())
    data.columns = [hdr.replace("('sum', 'Value',", "").replace(")", "").replace("'", "") \
                   for hdr in data.columns]

    data.drop('index', axis='columns', inplace=True)

    return create_dict(data['SeriesName'], data['Country'], data['Year'],data['Value'])