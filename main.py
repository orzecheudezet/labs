from BikeRepository import *
from Rent import *
from functions import *


print("Witmy w wypozyczalni rowerow.")
wybor = None
while wybor != 'q':
    print("1. Wyswietl wszystkie rowery.")
    print("2. Wypozycz rower.")
    print("3. Wyswietl wypozyczenia.")
    print("4. Oddaj rower.")
    wybor = input()
    if wybor == '1':
        bR1 = BikeRepository()
        lR1 = bR1.getAll()
        for i in lR1:
            print(i.nrId, i.kolor, i.rama, i.rozmiar, i.cena, i.dostepnosc)
    elif wybor == '2':
        bR1 = BikeRepository()
        lR1 = bR1.getAll()
        nrRezerwcji = (getReservationNumber())
        imie = input("Podaj imie.")
        nazwisko = input("Podaj nzwisko.")
        nrId = input("Podaj nrId roweru.")
        dataOd = input("Podaj date wypozyczenia.")
        dataDo = input("Podaj date zwrotu.")
        rent = Rent(nrRezerwcji, imie, nazwisko, nrId, dataOd, dataDo)
        for i in lR1:
            if i.nrId == nrId and i.dostepnosc == "1":
                rent.rentABike()
                i.dostepnosc = "0"

        f = open("D:\\Szkolenie\\WypozyczalniaRowerow\\rowery.txt", "w")
        for i in lR1:
            f.write(i.nrId + ";" + i.rama + ";" + i.kolor + ";" + i.rozmiar + ";" + i.cena + ";" + i.dostepnosc + "\n")

        f.close()

    elif wybor == '3':
        rents = getAllRents()
        for i in rents:
            print(i.nrRezerwacji, i.imie, i.nazwisko, i.nrId, i.dataOd, i.dataDo)

    elif wybor == '4':
        listaWyp = getAllRents()
        BR = BikeRepository()
        listaRowerow = BR.getAll()
        BR.returnBike(listaWyp, listaRowerow)







    else:
        print("Do widzenia.")