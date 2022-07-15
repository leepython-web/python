#Analog of admin base
level = 0       #Стандарнтый уровень доступа
login = ''
password = ''
while not login:
    login = input('Введите имя Вашей учетной записи: ')
while not password:
    password = input('Введите пароль от Вашей учтеной записи: ')

if login == 'admin' and password == 'root':
    level = 100
elif login == 'omnomnom' and password == 'baton':
    level = 99

if level:
    print('Добро пожаловать в игру,', login)
    print('Ваш ранг в игре: ', level)
else:
    print('Логин или пароль введены неверно, \n Доступ заблокирован!')
