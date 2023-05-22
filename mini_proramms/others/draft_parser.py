import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

result = []

URL_TEMPLATE = 'https://wildrift-wiki.com/assassins/283-riven.html'
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, 'html.parser')
characteristics = soup.find_all('table', class_='fr-solid-borders fr-alternate-rows')
for parametr in characteristics:
    result.append(f' {parametr.text}, ')

print(result)

