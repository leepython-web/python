#Привет, здесь я попробую создать рандомайзер с игровой механикой

import random #Подключаю модуль рандома

print('*' * 15, 'let\'s play russian roulette','*' * 15)
print('The rules are simple. Stay alive as long as possible and take a place in the ranking!')

score = 0
answer = 0

while True:
    answer = input('Enter a number between 1 and 6. Press q to exit')
    if answer == 'q':
        break
    rand = random.randint(0,6)
    if answer == rand:
        score += 1
        print('Congratulations! You move on to the next round. \n Your score is: ', score)
    else:
        print('Goodbye')






