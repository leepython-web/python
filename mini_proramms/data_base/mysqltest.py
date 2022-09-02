
import mysql.connector

name = input('Введите ваше имя: \n')
score = input('Ваш счет: \n')
def rating(name, score):

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='0000',
        database='userscore'
    )

    my_cursor = mydb.cursor()
    sql_formula = 'INSERT INTO userscoretab (username, score) VALUES (%s, %s)'
    user = (f'{name}', score)

    my_cursor.execute(sql_formula, user)

    mydb.commit()

rating(name, score)
