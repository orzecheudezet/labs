from functions import *
import datetime
import time

# dateString = '12-02-2019'
# dateString2 = '15-02-2019'
# dateObj = stringToDate(dateString)
# dateObj2 = stringToDate(dateString2)
#
# dateDelta = (dateObj2 - dateObj).days
# print(dateDelta)


czasTeraz = datetime.datetime.now()
print(czasTeraz)
dataTeraz = czasTeraz.date()
print(dataTeraz)


rents = getAllRents()
for i in rents:
    terminOddania = stringToDate(i.dataDo)
    if terminOddania < dataTeraz:
        print(i.nrRezerwacji, i.imie, i.nazwisko, i.nrId, i.dataOd, i.dataDo)