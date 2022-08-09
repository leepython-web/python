print('Для выхода из программы введите q')
def user_name():
    name = None
    count = 0
    txt = open('data.txt', 'w', encoding='utf-8')

    while name != 'q':
        count += 1
        name = input('Enter your name: ')
        txt.write(f'\n {count}) {name}')
    txt.close()

def read_user_name():
    txt = open('data.txt', 'r', encoding='utf-8')
    for line in txt:
        print(line)
    txt.close()

user_name()
read_user_name()
