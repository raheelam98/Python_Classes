import numpy as np
import pandas as pd
import ssl

print("Get url \n")

# Extracting Data from a URL

# Disable SSL certificate verification (not recommended for production)
ssl._create_default_https_context = ssl._create_unverified_context
#ssl.....    is used to disable SSL certificate 


url = "https://www.w3schools.com/python/python_operators.asp"
tables = pd.read_html(url)

# Check if any tables were found
if len(tables) > 0:
    # Access the first table (if there are multiple)
    result_table = tables[0]
    print(result_table)
else:
    print("No tables found on the webpage.")