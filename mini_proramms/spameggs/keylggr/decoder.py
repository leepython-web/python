import rsa

pubkey, privkey = rsa.newkeys(512)

message = ('HELLO MY DEAR FRIEND')



dectex = rsa.decrypt(enctex, privkey).decode()
print("The primordial string: ", message)

print("The Decrypted message: ", dectex)

def mainMenu():
    print('''Message senler v0.001. @All rights reserved
    1. Send message
    2. Decode message
    3. Keys''')
    menuInput = int(input())
    if menuInput == 1:
        print('Send message')
        sendMessage
    elif menuInput == 2:
        print('Decode message')
        decodeMessage
    elif menuInput == 3:
        print('Keys')
        keys
    else:
        print('Invalid input, please try again')

def sendMessage():
    print('Enter your message: ')
    message = str(input())
    enctex = rsa.encrypt(message.encode(), pubkey)
    print("The Encrypted message: ", enctex)
