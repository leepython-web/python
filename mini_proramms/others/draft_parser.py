import requests
from bs4 import BeautifulSoup as bs
import mysql.connector
from mysql.connector import connect, Error
from getpass import getpass

#URL_TEMPLATE = 'https://wildrift-wiki.com/assassins/283-riven.html'

def main_menu():
    menu_input = input('MAIN_MENU.\n1. Enter a URL.\n2. Enter a hero name.\n')
    if menu_input == '1':
        URL_TEMPLATE = input('Enter a URL: ')
        mysql_connect(URL_TEMPLATE)
    else:
        print('Try again')

def hero_parser(URL_TEMPLATE):
    result = []
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'html.parser')
    characteristics = soup.find('table', class_='fr-solid-borders fr-alternate-rows').find_all('td')
    for parametr in characteristics:
        result.append(parametr.text)
    return result

def mysql_connect(URL_TEMPLATE):
    result = hero_parser(URL_TEMPLATE)
    try:
        with connect(
            host='localhost',
            user=input('Enter your username: '),
            password=input('Enter your pass: '),
            #password=getpass('Enter your pass: '),
            database='wild_draft'
        ) as connection:
            insert_charact_query = f'''
            INSERT INTO wild_draft.infoheroes
            (IdHero, IdChar, Lvl_1, WhithLvl, Lvl_15)
            VALUES
                ({result[5]}, {result[6]}, {result[7]}),
                ({result[9]}, {result[10]}, {result[11]}),
                ({result[13]}, {result[14]}, {result[15]}),
                ({result[17]}, {result[18]}, {result[19]}),
                ({result[21]}, {result[22]}, {result[23]}),
                ({result[25]}, {result[26]}, {result[27]}),
                ({result[29]}, {result[30]}, {result[31]}),
                ({result[33]}, {result[34]}, {result[35]}),
                ({result[37]}, {result[38]}, {result[39]}),
                ({result[41]}, {result[42]}, {result[43]}),
            '''
            with connection.cursor() as cursor:
                cursor.execute(insert_charact_query)
                connection.commit()
    except Error as e:
        print(e)

main_menu()
#mysql_connect()
#hero_parser(URL_TEMPLATE)
