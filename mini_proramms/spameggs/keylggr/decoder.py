from cryptography.fernet import Fernet
import pyperclip
status = 0
def mainMenu():
    global status
    '''Меню: 1)sendMessage, 2) decodeMessage, 3)keys + перехват ошибок'''
    print('''\nMessage senler v0.002. @All rights reserved
    1. Send message
    2. Decode message
    3. Encryption key''')
    menuInput = input()
    if menuInput in ['1', '2'] and status < 1:
        print('Error. Firstly, generate or enter your encryption key!')
        return mainMenu()
    elif menuInput == '1':
        print('Send message')
        sendMessage()
    elif menuInput == '2':
        print('Decode message')
        decodeMessage()
    elif menuInput == '3':
        status = status + 1
        print('Keys')
        keys()
    else:
        print('Invalid input, please try again')
        return mainMenu()

def sendMessage():
    ''' На входе пользовательское сообщение которое надо ЗАшифровать. Шифруем через модуль FERNET по ранее сгенерированному
    ключу (mainMenu - keys - 1. Generate random key). Метод strip для обрезания строки'''
    print('Enter your message: ')
    message = str(input())
    enctex = fernet.encrypt(message.encode())
    enctexOutput = str(enctex).strip('b\'')
    print("The Encrypted message: ", enctexOutput)
    dataCopy(enctexOutput)
    return mainMenu()

def decodeMessage():
    ''' На входе пользовательское сообщение которое надо ДЕшифровать. Дешифруем через модуль FERNET по ранее сгенерированному
    ключу (mainMenu - keys - 1. Generate random key). Метод strip для обрезания строки
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
            print('Success!')
            return keys()
        case ('2'):
            keyOutput = str(key).strip('b\'')
            print(f'''Your encryption key: 
            {keyOutput}''')
            dataCopy(keyOutput)
        case ('3'):
            key = input('Enter a new key:\n')
        case _:
            print('Invalid input, please try again')
            return keys()
    fernet = Fernet(key)
    return mainMenu()

def dataCopy(menuSection):
    '''Функция dataCopy позволяет копировать содержимое заданной переменной в буфер обмена при нажатии любой кнопки'''
    menuInput = None
    while not menuInput:
        menuInput = input('Press anything key to copy:\n')
        pyperclip.copy(f'{menuSection}')
        print('Successfully copied!')

mainMenu()
