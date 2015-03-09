CREATE DATABASE Kalender;

CREATE TABLE Gruppe
	(GruppeID INT NOT NULL,
	ParentGroup INT,
	FOREIGN KEY(ParentGroup) REFERENCES Gruppe(GruppeID),
	PRIMARY KEY (GruppeID)
    );

CREATE TABLE Ansatt
	(Brukernavn VARCHAR(20) NOT NULL, 
     Passord VARCHAR(40) NOT NULL, 
     PRIMARY KEY (Brukernavn),
     );

CREATE TABLE Deltaker();

CREATE TABLE Møteleder();

CREATE TABLE Invitert();


     
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

CREATE TABLE Alarm
	(AlarmID INT NOT NULL,
    Tidspunkt VARCHAR(5) NOT NULL,
    AlarmType VARCHAR(25) NOT NULL,
    PRIMARY KEY (AlarmID), 
    FOREIGN KEY (AvtaleID) REFERENCES Avtale,
    FOREIGN KEY (Brukernavn) REFERENCES Ansatt );

    
% ALTER TABLE Orders
