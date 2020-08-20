"""
tests functions that collect dbpedia data
"""

import sys
here = sys.path[0]
sys.path.append(here[:len(here)-len("/tests")])

from dbpedia.helpers.download_raw_helper import *

def test_sys_path():
    """
    checks if data-collection directory is in path
    """
    out = False
    for path in sys.path:
        *_, path = path.split("/")
        if path == "data-collection":
            out = True
            
    assert out
    
def test_parse_page():
    """
    tests parse_page function againsts dummy url
    """
    test_url = "http://dbpedia.org/ontology/type"

    test = parse_page(test_url)

    assert len(test) == 8
    assert "rdf:type" in test.keys()
    assert "rdfs:label" in test.keys()
    assert len(test["rdf:type"]) == 2