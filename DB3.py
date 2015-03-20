__author__ = 'Monwa'

#!/usr/bin/python
import MySQLdb

# connect
db = MySQLdb.connect(host="78.91.36.170", user="Eivind", passwd="secret",
db="Kalender")
cursor = db.cursor()

# execute SQL select statement
choice = input("Tast inn foelgende \n - 1 for aa legge inn avtale \n - 2 for aa logge inn \n - 3 for aa se alle brukere som skal paa mote \n - 4 Se alle avtaler for alle ROM  ")

if choice == 1:
    print("Du valgte aa legge inn en avtale")
    Dato = raw_input("Skriv inn avtaledato (dd-mm-yyyy): ")
    StartTid = raw_input("Skriv inn starttid(hhmm): ")
    SluttTid = raw_input("Skriv inn slutttid(hhmm): ")
    Beskrivelse = raw_input("Skriv inn en Beskrivelse: ")

    cursor.execute("SELECT RomID, Kapasitet FROM Rom WHERE RomID NOT IN (SELECT RomID FROM Avtale WHERE Dato='03-04-2015' AND ((SluttTID>830 AND SluttTID<1230) OR (StartTID>830 AND StartTID<1230)))")
    cursor.execute("SELECT * FROM Rom")
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1])
    if not rows:
        print("Det er ingen ledige rom") #"+str(Dato)+" mellom "+str(StartTID)+"og "+str(SluttTid)+"
    RomID = raw_input("Skriv inn oensket RomID: ")

    print("Du valgte aa legge inn en avtale")
    Dato = input("Skriv inn avtaledato (dd-mm-yyyy): ")
    StartTid = input("Skriv inn starttid(hhmm): ")
    StoppTid = input("Skriv inn stopptid(hhmm): ")
    Beskrivelse = input("Skriv inn en Beskrivelse (\"beskrivelse\"): ")
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

elif choice == 3:
    print("Du valgte aa vise brukernavn etter gitt AvtaleID")
    ID = raw_input("Vennligst skriv inn AvtaleID: ")
    cursor.execute("SELECT Brukernavn FROM Deltaker WHERE DeltagerStatus = 'OK' AND AvtaleID = %s GROUP BY Brukernavn", (ID))
    for row in cursor:
        print row
elif choice == 4:
    print("Alle avtaler for alle rom")
    cursor.execute("SELECT * FROM Avtale JOIN Rom ON Avtale.RomID=Rom.RomID GROUP BY Rom.RomID,AvtaleID")
    for row in cursor:
        print row

elif choice == 5:
    print("Du har valgt aa slette en avtale paa dato med mindre enn oppgitt kapasitet")
    Dato = raw_input("Skriv inn avtaledato (dd-mm-yyyy): ")
    Kapasitet = raw_input("Skriv inn onsket makskapasitet: ")
    cursor.execute("SELECT AvtaleID FROM Avtale JOIN Rom ON Avtale.RomID=Rom.RomID WHERE (Dato=%s AND Kapasitet<%s)", (str(Dato),str(Kapasitet)))
    for row in cursor:
        print("Deleting AvtaleID "+str(row[0]))
        cursor.execute("alter table Avtale nocheck constraint all")
        cursor.execute("DELETE FROM Avtale WHERE AvtaleID = %s", row[0])
        cursor.execute("alter table Avtale check constraint all")


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
    #cursor.execute("SELECT Kapasitet FROM Rom WHERE RomID=%s", (RomID))
    #Kapasitet = cursor.fetchone()

    # Join, Group By og Having
    #cursor.execute("""SELECT * FROM Avtale
    #				INNER JOIN Rom
    #				WHERE StartTID > 0800
    #				GROUP BY StartTID
    #				""")
    #Update

    #cursor.execute("UPDATE Gruppe SET Beskrivelse='Supernerds' WHERE Beskrivelse = 'Nerds'")

    # Delete with join
    #cursor.execute("DELETE FROM Avtale JOIN Rom ON Avtale.RomID=Rom.RomID WHERE (Dato='03-04-2016' AND Kapasitet<10)")
    #cursor.execute("DELETE FROM Avtale JOIN Rom ON Avtale.RomID=Rom.RomID WHERE (Dato='03-04-2015' AND Kapasitet<20)")
    #cursor.execute("DELETE FROM Avtale JOIN Rom ON Avtale.RomID=Rom.RomID WHERE (Dato='1.1.2015' AND Kapasitet<30)")
    #For alle rom, list alle avtaler av en viss stoerrelse. RomID og antall arrangement mer enn x.
    # Send respons. Av inviterte til id, send invitasjoner.
    # Show all members of all groups
    # All appointments in all Room.
    # Status of all appointments
    # Finn paa litt morsomme spoerringer.
    #jangu@stud.ntnu.no


    # Insertion Avtale
    #cursor.execute("INSERT INTO Avtale (Dato, StartTid, SluttTid, Beskrivelse, RomID) VALUES (%s, %s, %s, %s, %s)", (Dato, StartTid, SluttTid, Beskrivelse, RomID))
    # Insertion moeteleder
    #cursor.execute("INSERT INTO Moteleder (Brukernavn, AvtaleID, Counter) VALUES ("Jens", 10, 24)")
    #cursor.execute("SELECT * FROM Avtale")
    #rows = cursor.fetchall()
    #for row in rows:
    #		print(row[0], row[1], row[2], row[3], row[4], row[5])


    #cursor.execute("SELECT * FROM Rom WHERE RomID NOT IN (SELECT RomID FROM Avtale WHERE Dato=%s AND ((SluttTID>%s AND SluttTID<%s) OR (StartTID>%s AND StartTID<%s))", (Dato, StartTid, SluttTid, StartTid, SluttTid))

    	# Noested spoerring
           	#SELECT * FROM Rom WHERE RomID NOT IN (SELECT RomID FROM Avtale WHERE Dato=03-04-2015 AND ((SluttTID>830 AND SluttTID<1230) OR (StartTID>830 AND StartTID<1230))
    #SELECT * FROM Rom WHERE RomID NOT IN(


    # Send en spoerring over ledige moeterom i tidspunktet
    #cursor.execute("SELECT RomID, Kapasitet FROM Avtale WHERE (Dato=%s AND (SluttTID>%s OR StartTID<%s)", (str(Dato), StartTid, StoppTid))