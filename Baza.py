import mysql.connector
listnum=[]
listword=[]
MySQL = mysql.connector.connect(
            host = 'localhost',
            user = 'Admin',
            passwd = 'admin',
            database = 'tlumacz')
cursor = MySQL.cursor()
cursor.execute('select * from pytania')
records = cursor.fetchall()
for row in records:
    listnum.append(row[0])
    listword.append(row[1])
print(listnum)
print(listword)