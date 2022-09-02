
import mysql.connector

score = input('Ваш счет: \n')

def range_table():
    name = input('Enter your name: ')
    rating(name, score)

def connecting():
    global mydb
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='0000',
        database='userscore')

def rating(name, score):

    connecting()

    my_cursor = mydb.cursor()
    sql_formula = 'INSERT INTO userscoretab (username, score) VALUES (%s, %s)'
    user = (f'{name}', score)
    my_cursor.execute(sql_formula, user)
    mydb.commit()

def read_range_table():
    connecting()
    my_cursor = mydb.cursor()
    sql_formula = 'SELECT * FROM userscoretab ORDER BY `score` DESC'
    my_cursor.execute(sql_formula)
    result = my_cursor.fetchall()
    for row in result:
        print(row)

read_range_table()
