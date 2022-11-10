from cryptography.fernet import Fernet

def mainMenu():
    '''Меню: 1)sendMessage, 2) decodeMessage, 3)keys + перехват ошибок'''

    print('''\n\nMessage senler v0.001. @All rights reserved
    1. Send message
    2. Decode message
    3. Encryption key''')
    menuInput = input()
    if menuInput == '1':
        print('Send message')
        sendMessage()
    elif menuInput == '2':
        print('Decode message')
        decodeMessage()
    elif menuInput == '3':
        print('Keys')
        keys()
    else:
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
    return mainMenu()

def decodeMessage():
    ''' На входе пользовательское сообщение которое надо ДЕшифровать. Дешифруем через модуль FERNET по ранее сгенерированному
    ключу (mainMenu - keys - 1. Generate random key. Метод strip для обрезания строки)'''
    print('Enter your encrypted message: ')
    message = str(input())
    dectex = fernet.decrypt(message).decode()
    print("The Decrypted message: ", dectex)
    return mainMenu()
def keys():
    '''Генерация ключа через модуль FERNET и его хранение'''
    print('''
    1. Generate random key
    2. Check your encryption key''')
    keyInput = input()
    if keyInput == '1':
        global key, fernet, keyOutput
        print('Generate random key')
        key = Fernet.generate_key()
        fernet = Fernet(key)
        keyOutput = str(key).strip('b\'')
        return keys()
    elif keyInput == '2':
        print(f'''Your encryption key: 
            {keyOutput}''')
    else:
        print('Invalid input, please try again')
        return keys()
    return mainMenu()

mainMenu()
