CREATE DATABASE Kalender;

CREATE TABLE Avtale
	(AvtaleID INT NOT NULL, 
    Dato VARCHAR (11) NOT NULL, 
    StartDATO VARCHAR(11) NOT NULL,
    SluttDATO VARCHAR(11) NOT NULL,
    Beskrivelse VARCHAR(225) NOT NULL,
    RomID INT,
	Kapasitet INT,
    PRIMARY KEY (AvtaleID)
	);

CREATE TABLE Gruppe
	(GruppeID INT NOT NULL,
	ParentGroup INT,
	FOREIGN KEY(ParentGroup) REFERENCES Gruppe(GruppeID),
	PRIMARY KEY (GruppeID)
    );

CREATE TABLE Ansatt
	(Brukernavn VARCHAR(20) NOT NULL, 
     Passord VARCHAR(40) NOT NULL, 
     PRIMARY KEY (Brukernavn)
     );

CREATE TABLE Alarm
	(AlarmID INT NOT NULL,
    Tidspunkt VARCHAR(5) NOT NULL,
    AlarmType VARCHAR(25) NOT NULL,
    Brukernavn VARCHAR(20) NOT NULL
    PRIMARY KEY (AlarmID), ,
    FOREIGN KEY (Brukernavn) REFERENCES Ansatt );

CREATE TABLE Deltaker
	(Brukernavn VARCHAR(20) NOT NULL,
    AvtaleID INT NOT NULL,
    DeltagerStatus BOOLEAN NOT NULL,
    PRIMARY KEY (Brukernavn, AvtaleID),
    FOREIGN KEY Brukernavn REFERENCES Ansatt,
    FOREIGN KEY AvtaleID REFERENCES Avtale);

CREATE TABLE Møteleder
	(Brukernavn VARCHAR(20) NOT NULL,
    AvtaleID INT NOT NULL,
    Counter INT NOT NULL, # To avoid equlaity between Møteleder and Deltaker
    PRIMARY KEY (Brukernavn, AvtaleID,Counter),
	FOREIGN KEY Brukernavn REFERENCES Ansatt,
	FOREIGN KEY AvtaleID REFERENCES Avtale);

CREATE TABLE Gruppemedlemmer(
	GruppeID INT NOT NULL,
	Brukernavn VARCHAR(20) NOT NULL,
	PRIMARY KEY (GruppeID, Brukernavn),
	FOREIGN KEY GruppeID REFERENCES Gruppe,
	FOREIGN KEY Brukernavn REFERENCES Ansatt);


CREATE TABLE Invitert(
	GruppeID INT NOT NULL,
	AvtaleID INT NOT NULL,
	PRIMARY KEY (GruppeID,AvtaleID),
	FOREIGN KEY AvtaleID REFERENCES Avtale,
	FOREIGN KEY GruppeID REFERENCES Gruppe);

CREATE TABLE AvtaleAlarmer(
	AvtaleID INT NOT NULL,
	AlarmID INT NOT NULL,
	PRIMARY KEY(AvtaleID, AlarmID),
	FOREIGN KEY (AvtaleID) REFERENCES Avtale,
	FOREIGN KEY (AlarmID) REFERENCES Alarm);