import mysql.connector
from tkinter import messagebox
import sys
import os
if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder.replace("\\Difficulties","")) # now your working dir is the parent folder of the script
    print(folder.replace("\\Difficulties",""))
sys.path.append("Database")
file = open(folder+'\\Database\\pytania.sql',encoding="utf-8")
sql = file.read()


MySQL = mysql.connector.connect(user='root', password='', host='localhost')
cursor = MySQL.cursor()
cursor.execute('DROP DATABASE `tlumacz`')
cursor.execute('CREATE DATABASE `tlumacz`')
MySQL = mysql.connector.connect(user='root', password='', host='localhost',database='tlumacz')
cursor = MySQL.cursor()

for result in cursor.execute(sql, multi=True):
  if result.with_rows:
    print("Rows produced by statement '{}':".format(
      result.statement))
    print(result.fetchall())
  else:
    print("Number of rows affected by statement '{}': {}".format(
      result.statement, result.rowcount))

MySQL.close()
messagebox.showinfo(title='Success',message='Baza danych była sukceśnie zainstalowana')
