#Analog of admin base
level = 0       #Стандарнтый уровень доступа
login = ''
password = ''
while not login:   #Пока пользователь не введет логин/пароль
    login = input('Введите имя Вашей учетной записи: ')
while not password:
    password = input('Введите пароль от Вашей учтеной записи: ')
#Дальше подключаем БД. Но пока что обойдемся так
if login == 'admin' and password == 'root':
    level = 100
elif login == 'omnomnom' and password == 'baton':
    level = 99
#Если связка логина/пароля есть в БД( level more than 0)
if level:
    print('Добро пожаловать в игру,', login)
    print('Ваш ранг в игре: ', level)
else:
    print('Логин или пароль введены неверно, \n Доступ заблокирован!')
