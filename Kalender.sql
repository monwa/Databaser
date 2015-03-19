CREATE DATABASE Kalender;
USE Kalender;


GRANT ALL PRIVILEGES ON Kalender.* TO 'Eivind'@'%' identified by 'secret';

CREATE TABLE Avtale(
	AvtaleID INT NOT NULL AUTO_INCREMENT, 
    Dato VARCHAR (11) NOT NULL, 
    StartTID VARCHAR(11) NOT NULL,
    SluttTID VARCHAR(11) NOT NULL,
    Beskrivelse VARCHAR(225) NOT NULL,
    PRIMARY KEY (AvtaleID)
);

CREATE TABLE Gruppe(
	GruppeID INT NOT NULL AUTO_INCREMENT,
	ParentGroup INT,
	FOREIGN KEY(ParentGroup) REFERENCES Gruppe(GruppeID),
	PRIMARY KEY (GruppeID)
);

CREATE TABLE Ansatt(
	Brukernavn VARCHAR(20) NOT NULL, 
	Passord VARCHAR(40) NOT NULL, 
	PRIMARY KEY (Brukernavn)
);

CREATE TABLE Alarm(
	AlarmID INT NOT NULL AUTO_INCREMENT,
    Tidspunkt VARCHAR(5) NOT NULL,
    AlarmType VARCHAR(25) NOT NULL,
    Brukernavn VARCHAR(20) NOT NULL,
    PRIMARY KEY (AlarmID),
    FOREIGN KEY (Brukernavn) REFERENCES Ansatt(Brukernavn)
);

CREATE TABLE Deltaker(
	Brukernavn VARCHAR(20) NOT NULL,
    AvtaleID INT NOT NULL,
    DeltagerStatus VARCHAR(10) NOT NULL,
    PRIMARY KEY (AvtaleID),
    FOREIGN KEY (Brukernavn) REFERENCES Ansatt(Brukernavn),
    FOREIGN KEY (AvtaleID) REFERENCES Avtale(AvtaleID) 
);

CREATE TABLE Møteleder(
	Brukernavn VARCHAR(20) NOT NULL,
    AvtaleID INT NOT NULL,
    Counter INT NOT NULL,
    PRIMARY KEY (Brukernavn, AvtaleID, Counter),
	FOREIGN KEY (Brukernavn) REFERENCES Ansatt(Brukernavn),
	FOREIGN KEY (AvtaleID) REFERENCES Avtale(AvtaleID)
);

CREATE TABLE Gruppemedlemmer(
	GruppeID INT NOT NULL,
	Brukernavn VARCHAR(20) NOT NULL,
	PRIMARY KEY (GruppeID, Brukernavn),
	FOREIGN KEY (GruppeID) REFERENCES Gruppe(GruppeID),
	FOREIGN KEY (Brukernavn) REFERENCES Ansatt(Brukernavn)
);


CREATE TABLE Invitert(
	GruppeID INT NOT NULL,
	AvtaleID INT NOT NULL,
	PRIMARY KEY (GruppeID,AvtaleID),
	FOREIGN KEY (AvtaleID) REFERENCES Avtale(AvtaleID),
	FOREIGN KEY (GruppeID) REFERENCES Gruppe(GruppeID)
);

CREATE TABLE AvtaleAlarmer(
	AvtaleID INT NOT NULL,
	AlarmID INT NOT NULL,
	PRIMARY KEY(AvtaleID, AlarmID),
	FOREIGN KEY (AvtaleID) REFERENCES Avtale(AvtaleID),
	FOREIGN KEY (AlarmID) REFERENCES Alarm(AlarmID)
);

CREATE TABLE Rom (
  RomID varchar(40) NOT NULL,
  Kapasitet varchar(40) NOT NULL,	
  PRIMARY KEY (RomID),
  FOREIGN KEY(AvtaleID) REFERENCES Avtale(AvtaleID)
);