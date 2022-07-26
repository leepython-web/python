# Здесь практика работы с текстами
import re

data = input('Введите ваше ФИО и дату рождения в формате ДД/ММ/ГГ \n')
data = re.split(r'[,;\s]\s*', data)     # re.split добавляет большей гибкости к разделителям
surname, name, patronymic, *date = data

print(name, date)
