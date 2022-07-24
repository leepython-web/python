# Здесь практика работы с текстами


data = input('Введите ваше ФИО и дату рождения в формате ДД/ММ/ГГ \n')
data = data.split()

surname, name, patronymic, *date = data

print(name,date)