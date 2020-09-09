from helper.common import *

def clean_dbpedia(data):

    def filter_useful_fields(data):
        """
        returns only fields in useful_fields set
        """
        useful_fields = set([
            'dbo:PopulatedPlace/areaTotal', 
            'dbo:areaTotal',
            'dbp:gdpNominal', 
            'dbp:gdpNominalPerCapita', 
            'dbp:gdpNominalYear', 
            'dbp:gdpPpp', 
            'dbp:gdpPppPerCapita', 
            'dbp:gdpPppYear', 
            'dbp:hdi', 
            'dbp:hdiYear', 
            'dbp:hdiChange', 
            'dbo:PopulatedPlace/populationDensity', 
            'dbo:populationDensity', 
            'dbp:hdiRank', 
            'dbp:areaRank', 
            'dbp:gini', 
            'dbp:giniYear', 
            'dbp:populationDensityRank', 
            'dbo:populationTotal', 
            'dbp:gdpPppRank', 
            'dbp:gdpNominalRank', 
            'dbp:gdpPppPerCapitaRank', 
            'dbp:gdpNominalPerCapitaRank',
        ])

        for country_name, country in data.items():
            data[country_name] = {k:v for k,v in country.items() if k in useful_fields}

        return data

    def clean_number(number):
        """
        cleans a number string into a float
            if number is list:
                return average of numbers inside
        """
        def remove_brackets(number):
            for i, ch in enumerate(number):
                if ch in "{[(":
                    return number[:i].strip()
            return number.strip()

        if type(number) == str:
            number = remove_brackets(number)
            try: return float(number)
            except: return number

        elif type(number) == list:
            numbers = [remove_brackets(n) for n in number]
            try: return sum([float(n) for n in numbers]) / len(numbers)
            except: return numbers

    data = filter_useful_fields(data)
    for country_name, country in data.items():
        for k, v in country.items():
            country[k] = clean_number(v)

    return data
