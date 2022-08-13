#   Привет, здесь я попробую создать рандомайзер с игровой механикой

import random, pickle, shelve
print('\n\n', '*' * 15, 'let\'s play Russian Roulette', '*' * 15)
print('The rules are simple. Stay alive as long as possible and take a place in the ranking!')

score = 0
death = 0

def range_table():
    name = input('Enter your name: ')
    winner =  str(name) + ' ' + str(score)
    range_file = open('score.txt', 'ab')
    pickle.dump(winner, range_file)
    range_file.close

def main_menu():
    answer = None
    while not answer:
        print('\n \t\t  MAIN MENU', '\n 1. Play Game \n 2. Records table \n\n Для выхода нажмите любую кнопку')
        answer = input()
        if answer == '2':
            read_range_table()
        elif answer == '1':
            start()
        else:
            break

def start():
    global score, death
    while True:
        answer = str(input('Enter a number between 1 and 6. Press q to exit \n\n'))
        rand = str(random.randint(1, 6))  # Генерирует случайное число в диапазоне (x,y)
        if answer == 'q':  # Выход из цикла
            range_table()
            break
        elif rand == answer:  # Если ты угадал число, то твой счет увеличивается
            score += 1
            print('Congratulations! You move on to the next round. \n Your score is: ', score)
        else:
            death += 1  # Счетчик смертей
            print(f'You died {death} times')
    print(f'Your score is {score}. But you died {death} times. See you next time!')

def read_range_table():
    range_file = open('score.txt', 'rb')
    range = pickle.load(range_file)
    range_file.close
    print('\n\n', '*' * 15, 'let\'s play Russian Roulette', '*' * 15, '\n', range)

main_menu()
