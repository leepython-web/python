# Здесь практика работы с текстами
import re

data = input('Введите ваше ФИО и дату рождения в формате ДД/ММ/ГГ \n')
new_data = re.split(r'[,;./\s]\s*', data)     # re.split добавляет большей гибкости к разделителям
surname, name, patronymic, *date = new_data

print(name, date)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')    # Создание маски для поиска с группами захвата
date = datepat.findall(data)
print('All dates: ', date)

def change_date():
    refactor = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', data)
    print('Another format of date: ', refactor)
change_date()
