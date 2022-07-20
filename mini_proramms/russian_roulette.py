#   Привет, здесь я попробую создать рандомайзер с игровой механикой

import random
print('*' * 15, 'let\'s play russian roulette','*' * 15)
print('The rules are simple. Stay alive as long as possible and take a place in the ranking!')

score = 0
death = 0

while True:
    answer = str(input('Enter a number between 1 and 6. Press q to exit \n\n\n'))
    rand = str(random.randint(1, 6))  #  Генерирует случайное число в диапазоне (x,y)
    if answer == 'q':   #   Выход из цикла
        break
    elif rand == answer:    #   Если ты угадал число, то твой счет увеличивается
        score += 1
        print('Congratulations! You move on to the next round. \n Your score is: ', score)
    else:
        death +=1   #   Счетчик смертей
        print(f'You died {death} times')
print(f'Your score is {score}. But you died {death} times. See you next time!')





