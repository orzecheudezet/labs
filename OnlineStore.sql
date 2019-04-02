CREATE DATABASE OnlineStore;

-- tables

CREATE TABLE Customers (
    PESEL char(11) NOT NULL PRIMARY KEY,
    FirstName varchar(100) NOT NULL,
	LastName varchar(100) NOT NULL,
    City varchar(100) NOT NULL,
	PostalCode varchar (20) NOT NULL,
	Street varchar(100) NOT NULL,
	StreeNumber varchar(20) NOT NULL,
	FlatNumber varchar (20),
	BirthDate date NOT NULL);

CREATE TABLE Orders (
    OrderId int NOT NULL IDENTITY(1,1) PRIMARY KEY,
	Products varchar(255) NOT NULL,
	OrderStatus varchar(50) NOT NULL, 
	FirstName varchar(100) NOT NULL,
	LastName varchar(100) NOT NULL,
    City varchar(100) NOT NULL,
	PostalCode varchar (20) NOT NULL,
	Street varchar(100) NOT NULL,
	StreeNumber varchar(20) NOT NULL,
	FlatNumber varchar (20));

CREATE TABLE Products (
    Barcode char(12) NOT NULL PRIMARY KEY,
	ProductName varchar(255) NOT NULL,
	ProductDescription varchar(255) NOT NULL,
	Price decimal(6,2) NOT NULL,
	AvailableQuantity int NOT NULL);
	

CREATE TABLE Basket (
	BasketId int NOT NULL IDENTITY(1,1) PRIMARY KEY,
	Products varchar(255),
	TotalQuantity int NOT NULL,
	Subtotal decimal(6,2),
	BasketStatus bit NOT NULL);

CREATE TABLE BasketProducts (
	Quantity int NOT NULL);


-- Foreign keys
	 
ALTER TABLE Orders
ADD PESEL char(11) NOT NULL FOREIGN KEY REFERENCES Customers(PESEL);

ALTER TABLE Basket
ADD PESEL char(11) NOT NULL FOREIGN KEY REFERENCES Customers(PESEL);

ALTER TABLE BasketProducts
ADD Barcode char(12) NOT NULL FOREIGN KEY REFERENCES Products(Barcode);

ALTER TABLE BasketProducts
ADD BasketId int NOT NULL FOREIGN KEY REFERENCES Basket(BasketId);



-- Adding product

INSERT INTO Products (Barcode, ProductDescription, Price, AvailableQuantity, ProductName)
VALUES ('123456789101', 'PlayStation Plus: 3 Month Membership | PS4 | PSN Download Code',
'90', '100', 'PS PLUS 3');

INSERT INTO Products (Barcode, ProductDescription, Price, AvailableQuantity, ProductName)
VALUES ('123456789102', 'PlayStation Plus: 12 Month Membership | PS4 | PSN Download Code',
'240', '100', 'PS PLUS 12');

INSERT INTO Products
VALUES ('123456789103',
 'PS4 RDR2 Bundle', 'Sony PlayStation 4 500GB Console (Black) with Red Dead Redemption 2 Bundle',
  '1200', '100');

SELECT * FROM Products;

--Deleting product

DELETE FROM Products
WHERE ProductName = 'PS PLUS 12';

--Editing product

UPDATE Products
SET Price = '95.00'
WHERE ProductName = 'PS PLUS 3';
 
--Showing products

SELECT * FROM Products;

-- Adding customer

INSERT INTO Customers (PESEL, FirstName, LastName, City, PostalCode, Street, StreeNumber,
 FlatNumber, BirthDate)
VALUES ('93061410930', 'Krzysztof', 'Orzechowski', '£Ûdü', '92-314', 'Przbyszewskiego',
 '258', '2', '1993-06-14');

INSERT INTO Customers (PESEL, FirstName, LastName, City, PostalCode, Street, StreeNumber,
 FlatNumber, BirthDate)
VALUES ('93061410931', 'Jacek', 'Bπk', '£Ûdü', '92-123', 'KiliÒskiego',
 '55', '12', '1966-05-12');

 SELECT * FROM Customers;

-- Deleting Customer

 DELETE FROM Customers
 WHERE PESEL = '93061410931';



-- Searching products by name

SELECT * FROM Products
WHERE ProductName like 'PS%'

-- Adding product to basket

ALTER TABLE Orders
DROP COLUMN Products;

ALTER TABLE Orders
ALTER COLUMN OrderStatus int NOT NULL;

ALTER TABLE OrderProducts
DROP COLUMN ProductId;


CREATE TABLE OrderProducts (
	OrderId int NOT NULL FOREIGN KEY REFERENCES Orders(OrderId),
	ProductId char(12) NOT NULL FOREIGN KEY REFERENCES Products(Barcode));

ALTER TABLE OrderProducts
ADD Quantity int NOT NULL;



SELECT * FROM Customers;

ALTER TABLE Basket
DROP COLUMN Products;

INSERT INTO Basket
VALUES ('0', '0', '0', '9306141093');

INSERT INTO Basket
VALUES ('0', '0', '1', '93061410931')



SELECT * FROM Basket;

ALTER TABLE BasketProducts
ADD Quantity int NOT NULL;

--Custonmer adds product to a basket

SELECT * FROM Products;

INSERT INTO BasketProducts
VALUES ('123456789102', '1', '1');

INSERT INTO BasketProducts
VALUES ('123456789101', '1', '2');

INSERT INTO BasketProducts
VALUES ('123456789103', '2', '3');

SELECT * FROM BasketProducts;

--Customer deletes product from a basket

DELETE FROM BasketProducts
WHERE Barcode = '123456789102'

INSERT INTO Orders
VALUES ('1', 'Krzysztof', 'Orzechowski', '£Ûdü', '92-218',
 'Tyrmanda', '8', '53', '93061410930');

SELECT * FROM Orders;

SELECT * FROM Products;

SELECT * FROM OrderProducts;

INSERT INTO OrderProducts
VALUES ('1', '123456789103', '1')

INSERT INTO OrderProducts
VALUES ('1', '123456789102', '1')

-- Seller wants to check orders

SELECT Orders.FirstName, Orders.LastName, Orders.PESEL, Products.ProductName,
 Products.Barcode, Orders.Street as 'Order Street', Customers.Street, OrderProducts.Quantity, Orders.OrderId
FROM Orders
LEFT JOIN OrderProducts
ON Orders.OrderId = OrderProducts.OrderId
LEFT JOIN Products
ON OrderProducts.ProductId = Products.Barcode
LEFT JOIN Customers
ON Orders.PESEL = Customers.PESEL;

-- Seller wants to change order status 

SELECT * FROM Orders

UPDATE Orders
SET OrderStatus = '2'
WHERE OrderId = '1';

-- Seller wants to konw what products were ordered for basket status is 1

SELECT * FROM Basket

SELECT Customers.FirstName, Customers.LastName, Products.ProductName, BasketProducts.Quantity
FROM Basket 
LEFT JOIN BasketProducts
ON Basket.BasketId = BasketProducts.BasketId
LEFT JOIN Products
ON BasketProducts.Barcode = Products.Barcode
LEFT JOIN Customers
ON Basket.PESEL = Customers.PESEL 
WHERE BasketStatus = '1'

-- Seller wants to konw what products were ordered for basket status is 0

SELECT Customers.FirstName, Customers.LastName, Products.ProductName, BasketProducts.Quantity
FROM Basket 
LEFT JOIN BasketProducts
ON Basket.BasketId = BasketProducts.BasketId
LEFT JOIN Products
ON BasketProducts.Barcode = Products.Barcode
LEFT JOIN Customers
ON Basket.PESEL = Customers.PESEL 
WHERE BasketStatus = '0'