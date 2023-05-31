import requests
from bs4 import BeautifulSoup as bs
from mysql.connector import connect, Error

def hero_parser(URL_TEMPLATE):
    result = []
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'html.parser')
    characteristics = soup.find('div', class_='sect-content').find_all('div', class_='th-title nowrap')
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
            database='wild_draft'
        ) as connection:
            for heroname in result:
                insert_charact_query = f'''
                INSERT INTO wild_draft.heroes
                (HeroName)
                VALUES
                    ({heroname})
                '''
                with connection.cursor() as cursor:
                    cursor.execute(insert_charact_query)
                    connection.commit()
    except Error as e:
        print(e)

mysql_connect('https://wildrift-wiki.com/tags/solo/')