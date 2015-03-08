CREATE DATABASE Kalender;

CREATE TABLE Gruppe
	(GruppeID INT NOT NULL,
	PRIMARY KEY (GruppeID)
    );

CREATE TABLE Ansatt
	(Brukernavn VARCHAR(20) NOT NULL, 
     Passord VARCHAR(40) NOT NULL, 
     PRIMARY KEY (Brukernavn)
     );
