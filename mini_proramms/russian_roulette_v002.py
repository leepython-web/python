#   Привет, здесь я попробую создать рандомайзер с игровой механикой

import random, re, mysql.connector
import mini_proramms.data_base.mysqltest as sqlbase
print('\n\n', '*' * 15, 'let\'s play Russian Roulette', '*' * 15)
print('The rules are simple. Stay alive as long as possible and take a place in the ranking!')

score = 0
death = 0

def main_menu(answer = None):
    """Главное меню, из которого можно выбрать новые функциональные пункты: 1. Начать Игру, 2. Открыть таблицу рекордов
    3. Выход из игры"""
    while not answer:
        print('\n \t\t  MAIN MENU', '\n 1. Play Game \n 2. Records table \n 3. Exit \n\n')
        answer = input()
        if answer == '1':
            start()
        elif answer == '2':
            read_range_table()
        elif answer == '3':
            print('Come back again!')
            break
        else:
            print('INCORRECT INPUT!')
            return main_menu()

def start():
    """"Функциональный пункт Начать игру. Принимает числовой пользовательский ввод от 1 до 6 и сравнивает его с рандомным числом этого же диапазона.
    Если есть совпадение пользователь получает +1 балл, иначе увеличивается счетчик смертей"""
    global score, death
    while True:
        answer = str(input('Enter a number between 1 and 6. Press q to exit \n\n'))
        rand = str(random.randint(1, 6))  # Генерирует случайное число в диапазоне (x,y)
        if answer == 'q':   # Выход из цикла
            range_table()  # Регистрация в таблице рекордов
            break
        elif rand == answer:  # Если ты угадал число, то твой счет увеличивается
            score += 1
            print('Congratulations! You move on to the next round. \n Your score is: ', score)
        else:
            death += 1  # Счетчик смертей
            print(f'You died {death} times')
    print(f'Your score is {score}. But you died {death} times. See you next time!')

def range_table():
    global score
    name = input('Enter your name: ')
    rating(name, score)
    return read_range_table()

def connecting():
    global mydb
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='0000',
        database='userscore')

def rating(name, score):

    connecting()

    my_cursor = mydb.cursor()
    sql_formula = 'INSERT INTO userscoretab (username, score) VALUES (%s, %s)'
    user = (f'{name}', score)
    my_cursor.execute(sql_formula, user)
    mydb.commit()

def read_range_table():
    connecting()
    my_cursor = mydb.cursor()
    sql_formula = 'SELECT * FROM userscoretab ORDER BY `score` DESC'
    my_cursor.execute(sql_formula)
    result = my_cursor.fetchall()
    print('*'*15, 'RATING', '*'*15)
    for row in result:
        print(row)
    go = input('\nPress anything to back into Main Menu \n')
    if go == 'q':
        main_menu('3')

main_menu()
