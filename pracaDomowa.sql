--PRACA DOMOWA

-- 1 Zrzucam klucze
ALTER TABLE Rents 
DROP CONSTRAINT FK__Rents__PESEL__3D5E1FD2;

ALTER TABLE Persons
DROP CONSTRAINT PK__Persons__4F16EE7E7DEEEFEA;

-- 2 Zmieniam dane
ALTER TABLE Persons
ALTER COLUMN PESEL char(11) NOT NULL;

ALTER TABLE Rents
ALTER COLUMN PESEL char(11) NOT NULL;

-- 3 Usuwam rekordy
DELETE FROM Persons;

-- 4 Dodaje klucze
ALTER TABLE Persons
ADD PRIMARY KEY (PESEL);

ALTER TABLE Rents
ADD FOREIGN KEY (PESEL) REFERENCES Persons(PESEL);

-- 5 Dodaje rekordy z powrotem
INSERT INTO Persons (PESEL, Address, FirstName, LastName) 
Values ('87031803637', 'Tylna 2a','Micha³','Czerski')
INSERT INTO Persons (PESEL, Address, FirstName, LastName) 
Values ('88101103352','Roweckiego 11','Dominik','Grzedowski')
INSERT INTO Persons (PESEL, Address, FirstName, LastName) 
Values ('93061410930','Tyrmanda 8','Krzysztof','Orzechowski')
INSERT INTO Persons (PESEL, Address, FirstName, LastName) 
Values ('86122202683','Tylna 2a', 'Izabela','Czerska')
INSERT INTO Persons (PESEL, Address, FirstName, LastName) 
Values ('86020716455','Krawiecka 12a','Rafa³', 'Ciechomski')

-- 6 Sprawdzam
SELECT * FROM Persons;

-- 7 Wrzucam typka
INSERT INTO Persons (PESEL, Address, FirstName, LastName)
Values ('           ', '     ', '   ', '   ');

SELECT * FROM Persons;

-- 8 Robie update
UPDATE Persons
SET PESEL = '11111111111', Address= 'Beverly Hills', FirstName ='John', LastName = 'Travolta'
WHERE PESEL = '           ';

SELECT * FROM Persons;

-- 9 Kolejny update
UPDATE Persons
SET Address= 'Los Angeles'
WHERE PESEL = '11111111111';

SELECT * FROM Persons;

