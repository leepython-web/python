import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = 'https://wildrift-wiki.com/assassins/283-riven.html'

def draft_parser(URL_TEMPALTE):
    result = []
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'html.parser')
    characteristics = soup.find('table', class_='fr-solid-borders fr-alternate-rows').find_all('td')
    for parametr in characteristics:
        result.append(parametr.text)
    print(result)

draft_parser(URL_TEMPLATE)
