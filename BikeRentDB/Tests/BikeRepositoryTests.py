import pyodbc
from Bike import *
from BikeRepository import *

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=BikeRents;Trusted_Connection=yes')
cursor = cnxn.cursor()

# bikeColor = 'Red'
# bikeSize = '28'
# bikeBrand = 'Giant'
#
# query = "INSERT INTO Bikes (Color, Size, Brand) VALUES('"+bikeColor+"', '"+bikeSize+"', '"+bikeBrand+"')"
#
# print(query)

bikeRep1 = BikeRepository(cursor)
rower1 = Bike(None, 'red', '28', 'Giant')

bikeRep1.save(rower1)

cnxn.commit()

cursor.close()
cnxn.close()