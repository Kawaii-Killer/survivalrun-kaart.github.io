# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an URL object
url = 'https://www.uvponline.nl/uvponlineU/index.php/uvproot/wedstrijdschema/2023'
# Create object page
df = pd.read_html(url)

print(df)
