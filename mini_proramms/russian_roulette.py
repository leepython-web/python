#   Привет, здесь я попробую создать рандомайзер с игровой механикой

import random, re, pickle, shelve
print('\n\n', '*' * 15, 'let\'s play Russian Roulette', '*' * 15)
print('The rules are simple. Stay alive as long as possible and take a place in the ranking!')

score = 0
death = 0

def main_menu():
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
    range_file = open('score.txt', 'r', encoding='utf-8')
    range_read = range_file.read()
    range = re.split(r'[,;./\s]\s*', range_read)
    *name, points = range
    print(name)
    #insertion_sort(points)
    range_file.close


def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            # Меняем местами число, продвигая по списку
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Остановимся и сделаем последний обмен
        arr[pos] = cursor

    return arr

rating()
