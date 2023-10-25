import mysql.connector
import sys
import os
from tkinter import messagebox
if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder) # now your working dir is the parent folder of the script
sys.path.append("Database")
MySQL = mysql.connector.connect(
	host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'mysql',
)
cursor = MySQL.cursor()
cursor.execute('Create database tlumacz')
MySQL2 = mysql.connector.connect(
	host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'tlumacz',
)
cursor2 = MySQL2.cursor()
with open(folder+'\\Database\\pytania.sql', 'r') as f:
	cursor2.execute(f.read(), multi=True)
cursor2.execute("CREATE USER 'Admin'@'localhost' IDENTIFIED BY 'admin'")
cursor2.execute("Grant all privileges on tlumacz to 'Admin'@'localhost'")
cursor2.execute("Grant all privileges on tlumacz.pytania to 'Admin'@'localhost'")
		