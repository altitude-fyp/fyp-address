import requests 
from bs4 import BeautifulSoup

def get_soup(url):
    r = requests.get(url)
    assert r.status_code == 200
    soup = BeautifulSoup(r.content, "html.parser")
    return soup

def read_table(table, custom_headers=False, edit_headers=None, verbose=False):
    """
    input: table BeautifulSoup object
    output: json representation of table

    eg. [
        {"header1": 123, "header2":234, "header3":345},
        {"header1": 456, "header2":567, "header3":897}, ...
    ]

    Parameters:

    custom_headers: List
        - if passed in, custom_headers will be assigned to headers variable

    edit_headers: function
        - if passed in, edit_headers(headers) function will be called
    """

    if custom_headers:
        headers = custom_headers
    else:
        headers = [th.text.strip() for th in table.find_all("th")]

    if edit_headers is not None:
        edit_headers(headers)
    
    out = []

    for tr in table.find_all("tr"):

        try:
            tds = tr.find_all("td")
            temp = {header:td.text.strip() for header,td in zip(headers,tds)}
            if temp: out.append(temp)

        except Exception as err:
            if verbose: print("ERROR:",str(err))
    
    return out