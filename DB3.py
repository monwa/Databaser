__author__ = 'Monwa'


#!/usr/bin/python
import MySQLdb

# connect
db = MySQLdb.connect(host="78.91.37.250", user="Eivind", passwd="secret",
db="Kalender")
cursor = db.cursor()

# execute SQL select statement
choice = input("Tast inn følende \n - Tast 1 for å legge inn avtale \n - Tast 2 for å ..") 

if choice = 1:
	print("Du valgte å legge inn en avtale")
	Dato = input("Skriv inn avtaledato (dd-mm-yyyy)")
	StartTid = input("Skriv inn starttid(hhmm)")
	StoppTid = input("Skriv inn stopptid(hhmm)")
	Beskrivelse = input("Skriv inn en Beskrivelse")
	# Send en spørring over ledige møterom i tidspunktet 
	cursor.execute("SELECT RomID, Kapasitet FROM Avtale WHERE StoppTid<"+StartTid" OR StartTid>"+StoppTid"")
	RomID = input("Skriv inn ønsket RomID")
	Kapasitet = "SELECT Kapasitet FROM Avtale"
	cursor.execute("INSERT INTO Avtale (Dato, StartTid, StoppTid, Beskrivelse, RomID, Kapasitet*/) VALUES (%s, %s, %s, %s, %s, %s)", (Dato, StartTid, StoppTid, Beskrivelse, RomID, Kapasitet))
if choice = 2:


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
	Kapasitet = cursor. Select Kapasitet from Rom where RomID = RomID.
