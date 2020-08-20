import os
import sys

here = sys.path[0]
home = here[:-len("/tests")]

def test_dotenv():
    """
        test if .env file is present in data-collection
        throws assertion error 
    """
    assert ".env" in os.listdir(home)
