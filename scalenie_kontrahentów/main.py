import pandas as pd
from Kontrahent import *

df = pd.read_excel('C:/Users/User/Desktop/LK/scalenie_kontrahentów2.xlsx', sheet_name='unikalny')

kontrahenci = df.values.tolist()



kontrahent1 = kontrahenci[1]
print(kontrahent1)