# Думаю в представлении не нуждается. Проба

board = list(range(1,10))

def board_create(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-' * 13)
board_create(board)

def take_input(input):
    valid = False
    while not valid:
        player_answer = input('Ваш ход на клетку: ' + input + '? ')
        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Это было не число, так ведь?) ')
            continue
        if player_answer in range (1,10):
            if (str(board[player_answer - 1]) not in 'XO'):
                board[player_answer - 1] = input
                valid = True
            else:
                print('Эта клетка уже занята, попробуйте другую ')
        else:
            print('Некорректный ввод. Пожалуйста, введите число от 1 до 9 ')

def check_win():

