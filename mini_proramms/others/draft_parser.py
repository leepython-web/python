import requests
from bs4 import BeautifulSoup as bs
import mysql.connector
from mysql.connector import connect, Error
from getpass import getpass

URL_TEMPLATE = 'https://wildrift-wiki.com/assassins/283-riven.html'

def hero_parser(URL_TEMPALTE):
    result = []
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'html.parser')
    characteristics = soup.find('table', class_='fr-solid-borders fr-alternate-rows').find_all('td')
    for parametr in characteristics:
        result.append(parametr.text)
    print(result)

def mysql_connect():
    try:
        with connect(
            host='localhost',
            user=input('Enter your username: '),
            password=input('Enter your pass: '),
            #password=getpass('Enter your pass: '),
            database='wild_draft'
        ) as connection:
            show_table_query = 'SHOW DATABASES'
            with connection.cursor() as cursor:
                cursor.execute(show_table_query)
                for tb in cursor:
                    print(tb)
    except Error as e:
        print(e)

mysql_connect()
#hero_parser(URL_TEMPLATE)
