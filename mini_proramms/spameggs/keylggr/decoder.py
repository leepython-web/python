from cryptography.fernet import Fernet

def mainMenu():
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
    print('Enter your message: ')
    message = str(input())
    enctex = fernet.encrypt(message.encode())
    print("The Encrypted message: ", enctex)
    return mainMenu()

def decodeMessage():
    print('Enter your encrypted message: ')
    message = str(input())
    dectex = fernet.decrypt(message).decode()
    print("The Decrypted message: ", dectex)
    return mainMenu()
def keys():
    print('''
    1. Generate random key
    2. Check your encryption key''')
    keyInput = input()
    if keyInput == '1':
        global key, fernet
        print('Generate random key')
        key = Fernet.generate_key()
        fernet = Fernet(key)
        return keys()
    elif keyInput == '2':
        print(f'''Your encryption key: 
            {key}''')
    else:
        print('Invalid input, please try again')
        return keys()
    return mainMenu()

mainMenu()
