import requests
from bs4 import BeautifulSoup
import sys



## checks for url in command parameters and sets as url:

url = None
if (len(sys.argv) == 2):
    url = str(sys.argv[1]).rstrip()
else:
    print('no url')
    exit()

print("=========================================")

print(f"url given: {sys.argv[1]}")

print("=========================================")

# gets the page and stores the data got back in response variable (response object complete)
#creates a soup(parsed html) in the variable named soup for parsing:

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

## finds the table with class "infobox and biota" identified from page html:

table = soup.find("table", class_="infobox biota")

## raw stores the text from all <td> tags in table:

raw = []

# the following loop goes throught the table to find all <td> tags and and populates the raw array with td.text:

for table_data in table.find_all('td'):

    ## removing the white space and ":" found in td.text then populating:

    cleaned = table_data.text.rstrip()
    rm = cleaned.replace(":", " ")
    raw.append(rm.strip())

## following row converts the data from raw array into a dict(final) for easy access:

raw_length = len(raw) - 1
final = {}
for i in range(0, raw_length, 2):

    ## checks and replaces first key which is empty due to one value in html table with name key
    ## while for others have field names already specified:

    if (raw[i] == ""):
        final['Name'] = raw[i + 1]
    else:
        final[raw[i]] = raw[i + 1]

## finally prints the keys and values in dict(final) - or all the processed data:
print('<==================================================================================>\n')

for keys in final:
    print(f"{keys}: {final[keys]}")

print('<==================================================================================>\n')
