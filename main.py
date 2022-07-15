# This is a simple calculator
print('*' * 15, 'Calculator', '*' * 10)
print('Press q to exit')
while True:
    sign = input('Enter a sign: +, -, *, /')
    if sign == 'q':
        break
    if sign in ('+','-','*','/'):
        x = float(input('Enter a value of x: '))
        y = float(input('Enter a value of y: '))
        if sign == '+':
            print('Answer is: ', x+y)
        if sign == '-':
            print('Answer is: ', x-y)
        if sign == '*':
            print('Answer is: ', x*y)
        if sign == '/':
            print('Answer is: ', x/y)
    else:
        print('Error: invalid sign of operation')