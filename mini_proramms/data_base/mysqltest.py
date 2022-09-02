
import mysql.connector

def rating():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='0000',
        database='userscore'
    )

    my_cursor = mydb.cursor()
    sql_formula = 'INSERT INTO userscoretab (username, score) VALUES (%s, %s)'
    user1 = ('Максим', 12)

    my_cursor.execute(sql_formula, user1)

    mydb.commit()
