__author__ = 'Monwa'


#!/usr/bin/python
import MySQLdb

# connect
db = MySQLdb.connect(host="78.91.37.250", user="Eivind", passwd="secret",
db="Kalender")
cursor = db.cursor()

# execute SQL select statement
statements = []
statements.append("SELECT * FROM AVTALE")
statements.append("INSERT INTO ANSATT" "")
statements.append("SELECT * FROM ANSATT")
#statements.append("UPDATE AVTALE, SET Dato='20/03/2015', WHERE AvtaleID='1'")


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
