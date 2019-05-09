CREATE DATABASE BikeRents;

USE BikeRents

CREATE TABLE Bikes (
Id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
Color varchar(50) NOT NULL,
Size int NOT NULL,
Brand varchar(50) NOT NULL);

INSERT INTO Bikes (Id, Color, Size, Brand)
VALUES()