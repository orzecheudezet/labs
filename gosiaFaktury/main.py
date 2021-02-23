import pyodbc
import pandas as pd

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-KOMPUTER\SQLEXPRESS;DATABASE=gosiaFaktury;Trusted_Connection=yes')
cursor = cnxn.cursor()

data = pd.read_excel (r'C:\Users\user\Desktop\raport_U099_2020-09-21.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
df = pd.DataFrame(data, columns= ['NUMER'])
fd = pd.DataFrame(data, columns= ['UWAGI'])

print (fd)

listaLP = list(df.NUMER)

listaUwag = list(fd.UWAGI)
k=0

for item in listaLP:


    cursor.execute("INSERT INTO faktury (numerListu, uwagi) VALUES""('"+str(item)+"', '"+str(listaUwag[k])+"')")
    k = k +1

    cnxn.commit()
cursor.close()
cnxn.close()