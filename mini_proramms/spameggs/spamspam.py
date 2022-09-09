# Программа написана исключительно в целях проверки собственных устройств, автор не несeт ответсвенности за ее применение
import time, pyautogui

def sendMessage():
    time.sleep(2)
    message = 'EGGS EGGS EGGS'
    iterations = 10

    for i in range(iterations):
        pass

    while iterations > 0:
        iterations -= 1

    pyautogui.typewrite(message.strip())
    pyautogui.press('enter')

print('Получатель получил свинцовую пулю')

def SendText():
    time.sleep(3)
    with open('eggs.txt') as f: # Открывает блокнот с названием text.txt (документ с содержанием того, что мы хотим отправлять).
        lines = f.readline()
    for line in lines:
        pyautogui.typewrite(line.strip()) # В этой функции оно будет писать текст с каждой строки
        pyautogui.typewrite('enter') # и так же отправлять его "жертве".
    print("Дело сделано, осталось успокоить нашу жертву ^_^")

print('~'*50)
print("[1] ===> Стрелять одним сообщением указанным в переменной ")
print("[2] ===> Отправлять строки из блокнота ")
print('~'*50)
option = input("[Выбирай функцию]===> ")

if option == "1":
    sendMessage()
elif option == "2":
    SendText()
else:
    print('Выбирай функция 1 или 2!')


