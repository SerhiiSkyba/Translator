import mysql.connector
MySQL = mysql.connector.connect(
	host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'mysql',
)
cursor = MySQL.cursor()
try:
	cursor.execute('Create database tlumacz')
except:
	MySQL2 = mysql.connector.connect(
		host = 'localhost',
	    user = 'root',
	    passwd = '',
	    database = 'tlumacz',
	)
	cursor2 = MySQL2.cursor()
	try:
		cursor2.execute('CREATE TABLE `pytania` (`Nr` int(11) NOT NULL,`slowo` text COLLATE utf8_polish_ci NOT NULL)')
	except:
		cursor2.execute('Select * from `pytania`')
		cursor2.execute("INSERT INTO `pytania` (`Nr`, `slowo`) VALUES (1, 'jabłko'), (2, 'samochód'), (3, 'rower'), (4, 'pomarancza'), (5, 'drzwi'), (6, 'mieć'), (7, 'banan'), (8, 'potrafić'), (9, 'okno'), (10, 'pytanie'),(11, 'pies'),(12, 'kot'),(13, 'jeść'),(14, 'nowy'),(15, 'stary'),(16, 'tekst'),(17, 'nauka'),(18, 'temat'),(19, 'lekcja'),(20, 'język'),(21, 'tablet'),(22, 'klawiatura'),(23, 'samolot'),(24, 'hulajnoga'),(25, 'kabel'),(26, 'zasilać'),(27, 'kanapka'),(28, 'kodować'),(29, 'rysunek '),(30, 'pięć'),(31, 'nowoczesny'),(32, 'morze'),(33, 'woda'),(34, 'ocean'),(35, 'oko'),(36, 'ręka'),(37, 'plecak'),(38, 'bluza'),(39, 'kurtka'),(40, 'papier ');")
