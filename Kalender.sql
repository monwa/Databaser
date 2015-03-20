
USE Kalender;


GRANT ALL PRIVILEGES ON Kalender.* TO 'Eivind'@'%' identified by 'secret';


CREATE TABLE Rom (
	RomID INT(10) NOT NULL,
	Kapasitet VARCHAR(40) NOT NULL,	
	PRIMARY KEY (RomID)
);

CREATE TABLE Avtale (
  AvtaleID INT(11) NOT NULL AUTO_INCREMENT,
  Dato VARCHAR(11) NOT NULL,
  StartTID VARCHAR(11) NOT NULL,
  SluttTID VARCHAR(11) NOT NULL,
  Beskrivelse VARCHAR(225) NOT NULL,
  RomID INT(10) NOT NULL,
  PRIMARY KEY (AvtaleID),
  FOREIGN KEY (RomID) REFERENCES Rom(RomID)
);
CREATE TABLE Gruppe(
	GruppeID INT NOT NULL AUTO_INCREMENT,
	ParentGroup INT,
	Beskrivelse VARCHAR(225),
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
	Dato VARCHAR(11) NOT NULL,
    Tidspunkt VARCHAR(5) NOT NULL,
    AlarmType VARCHAR(25) NOT NULL,
    Brukernavn VARCHAR(20) NOT NULL,
    PRIMARY KEY (AlarmID),
    FOREIGN KEY (Brukernavn) REFERENCES Ansatt(Brukernavn)
);

CREATE TABLE Deltaker(
	Brukernavn VARCHAR(20) NOT NULL,
    AvtaleID INT(11) NOT NULL,
    DeltagerStatus VARCHAR(10) NOT NULL,
    PRIMARY KEY (AvtaleID, Brukernavn),
    FOREIGN KEY (Brukernavn) REFERENCES Ansatt(Brukernavn),
    FOREIGN KEY (AvtaleID) REFERENCES Avtale(AvtaleID) 
);

CREATE TABLE Møteleder(
	Brukernavn VARCHAR(20) NOT NULL,
    AvtaleID INT(10) NOT NULL,
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

