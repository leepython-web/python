from cryptography.fernet import Fernet
import pyperclip, time

def mainMenu():
    '''Меню: 1)sendMessage, 2) decodeMessage, 3)keys + перехват ошибок'''

    print('''\n\nMessage senler v0.002. @All rights reserved
    1. Send message
    2. Decode message
    3. Encryption key''')
    menuInput = input()
    match menuInput:
        case ('1'):
            print('Send message')
            sendMessage()
        case ('2'):
            print('Decode message')
            decodeMessage()
        case ('3'):
            print('Keys')
            keys()
        case _:
            print('Invalid input, please try again')
            return mainMenu()
def sendMessage():
    ''' На входе пользовательское сообщение которое надо ЗАшифровать. Шифруем через модуль FERNET по ранее сгенерированному
    ключу (mainMenu - keys - 1. Generate random key. Метод strip для обрезания строки)'''
    print('Enter your message: ')
    message = str(input())
    enctex = fernet.encrypt(message.encode())
    enctexOutput = str(enctex).strip('b\'')
    print("The Encrypted message: ", enctexOutput)
    dataCopy(enctexOutput)
    return mainMenu()

def decodeMessage():
    ''' На входе пользовательское сообщение которое надо ДЕшифровать. Дешифруем через модуль FERNET по ранее сгенерированному
    ключу (mainMenu - keys - 1. Generate random key. Метод strip для обрезания строки
    Дрбавлена функция dataCopy)'''
    print('Enter your encrypted message: ')
    message = str(input())
    dectex = fernet.decrypt(message).decode()
    print("The Decrypted message: ", dectex)
    return mainMenu()
def keys():
    '''Генерация ключа через модуль FERNET и его хранение'''
    print('''
    1. Generate random key
    2. Check your encryption key
    3. Enter a new key''')
    keyInput = input()
    match keyInput:
        case ('1'):
            global key, fernet, keyOutput
            print('Generate random key')
            key = Fernet.generate_key()
            fernet = Fernet(key)
            print('Success!')
            return keys()
        case ('2'):
            keyOutput = str(key).strip('b\'')
            print(f'''Your encryption key: 
            {keyOutput}''')
            dataCopy(keyOutput)
        case ('3'):
            key = input('Enter a new key')
            fernet = Fernet(key)
        case _:
            print('Invalid input, please try again')
            return keys()
    return mainMenu()

def dataCopy(menuSection):
    '''Функция dataCopy позволяет копировать содержимое заданной переменной в буфер обмена при нажатии любой кнопки'''
    menuInput = None
    while not menuInput:
        menuInput = input('Press anything key to copy')
        pyperclip.copy(f'{menuSection}')
        time.sleep(1)
        print('Successfully copied!')

mainMenu()
