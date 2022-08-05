# Пробую создать RSS ленту по url

def rss_reader (url):
    from urllib.request import urlopen
    # from xml.etree.ElementTree import parse

    # Загружаем RSS ленту и парсим ее
    u = urlopen(url)
    print(u)
    '''doc = parse(u)
    # Извлекаем RSS - ленту и парсим ее
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        print(title)
        print(date)
        print(link)
        print()'''

rss_reader('https://sys-adm.in/?format=feed&type=rss')