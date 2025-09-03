

print("Read python\n")

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send an HTTP request to the URL
url = 'https://www.w3schools.com/python/python_operators.asp'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table element(s) using the appropriate HTML tags and attributes
    tables = soup.find_all('table')

    # Iterate through the tables and read them into a list of DataFrames
    dfs = []
    for table in tables:
        df = pd.read_html(str(table))[0]
        dfs.append(df)

    # Access the first DataFrame
    if len(dfs) > 0:
        result_table = dfs[0]
        print(result_table)
    else:
        print("No tables found on the webpage.")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

