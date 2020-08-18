def extract_urls(d, out=set()):
    """
        As structure of input object may be inconsistent (random dictionaries or lists may pop up),
        this function is needed to parse through and extract the urls

        What this function does:
            1. extract all urls starting with http:// or https:// from within object recursively
            2. returns unique list of urls
    """

    if type(d) == dict:
        for k,v in d.items():
            if type(k) == str and k[:7] == "http://":
                out.add(k)

            if type(v) == str and v[:7] == "http://":
                out.add(v)
            
            if type(v) == dict or type(v) == list:
                extract_urls(v, out=out)

    elif type(d) == list:
        for i in d:
            if type(i) == str and i[:7] == "http://":
                out.add(i)

            if type(i) == dict or type(i) == list:
                extract_urls(i, out=out)

    return list(out)

if __name__ == "__main__":
    test = {
        "a": {
            "b": [
                "http://abc.com", 
                "wuhu",
                {"abdiwabdw": "http://dauywudh"},
                [
                    {"http://dwuagd": 2134}
                ]
            ]
        }, 
        
        "b": [
            "http://dwaiuhda",
            "http://diuwhaiu",
            {"http://dwhaid": 321}
        ]
    }

    urls = extract_urls(test)
    print(urls)