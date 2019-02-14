from functions import *
import datetime
import time

dateString = '12-02-2019'
dateString2 = '15-02-2019'
dateObj = stringToDate(dateString)
dateObj2 = stringToDate(dateString2)

dateDelta = (dateObj2 - dateObj).days
print(dateDelta)
