__author__ = 'Monwa'


#!/usr/bin/python
import MySQLdb

# connect
db = MySQLdb.connect(host="78.91.37.250", user="Eivind", passwd="secret",
db="Kalender")
cursor = db.cursor()

# execute SQL select statement
statements = []
statements.append("SELECT * FROM Avtale")
statements.append("INSERT INTO Ansatt (Brukernavn, Passord) VALUES ('Gretha', 'Grethatheta')")
statements.append("SELECT * FROM Ansatt")
#statements.append("UPDATE AVTALE, SET Dato='20/03/2015', WHERE AvtaleID='1'")

#(Gretha, Hans, BrodreneDahl, BarackObahamas, DonaldDuck)
#(Hansilove, Grethatheta, utpaaturaldrisur, USA, Quack)")


for statement in statements:
	print(statement)
	cursor.execute(statement)

# commit your changes
db.commit()

# get the number of rows in the resultset
numrows = int(cursor.rowcount)

# get and display one row at a time.
for x in range(0,numrows):
    row = cursor.fetchone()
    print row[0], "-->", row[1]
