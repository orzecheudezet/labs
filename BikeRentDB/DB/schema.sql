create database BikeRents;

CREATE TABLE Bikes (
Id int NOT NULL IDENTITY(1,1) PRIMARY KEY,
Color varchar(50) NOT NULL,
Size int NOT NULL,
Brand varchar(50) NOT NULL);