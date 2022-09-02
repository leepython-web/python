#   Привет, здесь я попробую создать рандомайзер с игровой механикой

import random, re, pickle, shelve
print('\n\n', '*' * 15, 'let\'s play Russian Roulette', '*' * 15)
print('The rules are simple. Stay alive as long as possible and take a place in the ranking!')

score = 0
death = 0

def main_menu():
    """Главное меню, из которого можно выбрать новые функциональные пункты: 1. Начать Игру, 2. Открыть таблицу рекордов
    3. Выход из игры"""
    answer = None
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
    """"Функциональный пунтк Начать игру. Принимает числовой пользовательский ввод от 1 до 6 и сравнивает его с рандомным числом этого же диапазона.
    Если есть совпадение пользователь получает +1 балл, иначе увеличивается счетчик смертей"""
    global score, death
    while True:
        answer = str(input('Enter a number between 1 and 6. Press q to exit \n\n'))
        rand = str(random.randint(1, 6))  # Генерирует случайное число в диапазоне (x,y)
        if answer == 'q':   # Выход из цикла
            range_table()   # Регистрация в таблице рекордов
            break
        elif rand == answer:  # Если ты угадал число, то твой счет увеличивается
            score += 1
            print('Congratulations! You move on to the next round. \n Your score is: ', score)
        else:
            death += 1  # Счетчик смертей
            print(f'You died {death} times')
    print(f'Your score is {score}. But you died {death} times. See you next time!')

def range_table():
    name = input('Enter your name: ')
    winner = str(name) + ' ' + str(score) + '\n'
    range_file = open('score.txt', 'a', encoding='utf-8')
    range_file.write(winner)
    range_file.close

def read_range_table():
    range_file = open('score.txt', 'r', encoding='utf-8')
    range = range_file.read()
    print('\n\n', '*' * 15, 'Record Table', '*' * 15, '\n', range)
    range_file.close

def rating():
    global score, death
    count = 0
    range_file = open('score.txt', 'r', encoding='utf-8')
    range_read = range_file.read()
    range = re.split(r'[,;./\s]\s*', range_read)
    new_range = []
    for i in range:
        count += 1
        if count %2 ==0:
            new_range.append(i)
        print(new_range)
    result = [int(item) for item in new_range]  #Преобразование списка в числа
    print(result.sort())

    range_file.close

main_menu()
