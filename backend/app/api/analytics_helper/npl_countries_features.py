import pickle
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def get_npl_country_npl_features(countryname):
    """
    input: country name (e.g Singapore)
    output: returns top 10 features correlating to the bank nonperforming loans to total gross loans (%)
    """
        
    all_country_data = pickle.load(open("pickled/autoregressed_country_data.sav", "rb"))

    country_data = {}

    for country, country_object in all_country_data.items():
        if country == countryname:
            country_data = country_object

    if country_data == {}:
        return 0

    similarity = {}

    npl_data = np.array(list(map(list, country_data['Bank nonperforming loans to total gross loans (%)'].items())))

    for indicator, time_series in country_data.items():
        indicator_data = np.array(list(map(list, time_series.items())))
        distance, path = fastdtw(npl_data, indicator_data, dist=euclidean)
        similarity[indicator] = distance

    sorted_similarity = dict(sorted(similarity.items(), key=lambda kv: kv[1])[1:11])

    return sorted_similarity