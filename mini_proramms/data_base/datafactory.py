
def user_name():
    name = None
    count = 0
    txt = open('data.txt', 'w', encoding='utf-8')

    while name != 'q':
        count += 1
        name = input('Enter your name: ')
        txt.write(f'\n {count}) {name}')
    txt.close()
user_name()
