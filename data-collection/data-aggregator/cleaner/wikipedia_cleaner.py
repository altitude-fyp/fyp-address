from helper.common import *

def clean_wikipedia(wikipedia):
    """
    clean only feature values under main column of each feature
    """

    def clean_number(number):

        def clean_bracket(number):
            for i, ch in enumerate(number):
                if ch in "[{(":
                    return number[:i].strip()
            return number.strip()

        number = clean_bracket(number)

        number = number.replace(",", "").replace(" ", "")

        multiplier = 1
        if "%" in number:
            number = number.replace("%", "")
            multiplier *= 0.01

        def handle_range(number):
            # eg. ranges like 3000-8000 -> 5000
            a,b = number.split("-")
            a,b = float(a), float(b)
            return (a+b)/2

        if number[0] != "-" and "-" in number:
            return handle_range(number)

        return float(number) * multiplier

    total = 0
    error = 0

    for feature in wikipedia:
        
        for row in feature["data"]:

            main = feature["main"]

            if type(main) != list:
                main = [main]

            for k in main:
                try: 
                    row[k] = clean_number(row[k])
                except: 
                    row[k] = None
                    error += 1
                total += 1

    # print(error, total)
    return wikipedia