__author__ = 'Monwa'


#!/usr/bin/python
import MySQLdb

# connect
db = MySQLdb.connect(host="129.241.165.185", user="Eivind", passwd="secret",
db="Kalender")
cursor = db.cursor()

# execute SQL select statement
choice = input("Tast inn foelgende \n - 1 for aa legge inn avtale \n - 2 for aa logge inn \n "+
	"..") 

if choice == 1:
	print("Du valgte aa legge inn en avtale")
	Dato = input("Skriv inn avtaledato (dd-mm-yyyy): ")
	StartTid = input("Skriv inn starttid(hhmm): ")
	StoppTid = input("Skriv inn stopptid(hhmm): ")
	Beskrivelse = input("Skriv inn en Beskrivelse (\"beskrivelse\"): ")
	# Send en spoerring over ledige moeterom i tidspunktet 
	#cursor.execute("SELECT RomID, Kapasitet FROM Avtale WHERE (Dato=%s AND (SluttTID>%s OR StartTID<%s)", (str(Dato), StartTid, StoppTid))
	cursor.execute("SELECT * FROM Rom")
	rows = cursor.fetchall()
	for row in rows:
    		print(row.RomID, row.Kapasitet)
	RomID = input("Skriv inn oensket RomID: ")
	Kapasitet = "SELECT Kapasitet FROM Avtale"
	cursor.execute("INSERT INTO Avtale (Dato, StartTid, StoppTid, Beskrivelse, RomID, Kapasitet*/) VALUES (%s, %s, %s, %s, %s, %s)", (Dato, StartTid, StoppTid, Beskrivelse, RomID, Kapasitet))
	db.commit()
elif choice == 2:
	global loggedIn
	print("Du valgte aa logge inn")
	Brukernavn = raw_input("Vennligst oppgi brukernavn: ")
	Passord = raw_input("Vennligst oppgi passord for brukeren " + Brukernavn + ": ")
	cursor.execute("SELECT * FROM Ansatt")
	for row in cursor:
			if (row[0] == Brukernavn and row[1] == Passord):
    				loggedIn = True
    				print("Succesfully logged in!\n")

	

#statements = []
#statements.append("SELECT * FROM Avtale")
#statements.append("INSERT INTO Ansatt (Brukernavn, Passord) VALUES ('Gretha', 'Grethatheta')")
#statements.append("SELECT * FROM Ansatt")
#statements.append("UPDATE AVTALE, SET Dato='20/03/2015', WHERE AvtaleID='1'")

#(Gretha, Hans, BrodreneDahl, BarackObahamas, DonaldDuck)
#(Hansilove, Grethatheta, utpaaturaldrisur, USA, Quack)")


#for statement in statements:
#	print(statement)
	#cursor.execute(statement)

# commit your changes
db.commit()

# get the number of rows in the resultset
#numrows = int(cursor.rowcount)

# get and display one row at a time.
#for x in range(0,numrows):
    #row = cursor.fetchone()
    #print row[0], "-->", row[1]
	#Kapasitet = cursor. Select Kapasitet from Rom where RomID = RomID.
