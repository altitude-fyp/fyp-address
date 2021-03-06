from helper.common import *

def clean_dbpedia(data):

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

    def clean_key(key):
        """
        cleans a string key 
            eg. dbo:areaTotal -> Area Total
        """
        key = key[4:]
        key = key[0].upper() + key[1:]

        def convert(string):
            out = []
            uppercase = set("abcdefghijklmnopqrstuvwxyz".upper())

            temp = ""
            for ch in string:
                if ch in uppercase:
                    out.append(temp)
                    temp = ch
                else:
                    temp += ch
            
            out.append(temp)

            return " ".join([i for i in out if i])

        return convert(key).lower()

    for country_name, country in data.items():
        data[country_name] = {clean_key(k): clean_number(v) for k,v in country.items()}

    return data
