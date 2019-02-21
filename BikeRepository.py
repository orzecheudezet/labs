from Bike import *
from functions import *
import datetime


class BikeRepository:



    def getAll(self):
        textFile = open("rowery.txt", "r")
        calosc = textFile.read()
        a = calosc.splitlines()
        listaRowerow = []
        for line in a:
            d = line.split(";")
            nrId = d[0]
            kolor = d[1]
            rama = d[2]
            rozmiar = d[3]
            cena = d[4]
            dostepnosc = d[5]
            bike = Bike(nrId, kolor, rama, rozmiar, cena, dostepnosc)
            listaRowerow.append(bike)
        textFile.close()
        return listaRowerow

    def returnBike(self, listaWyp, listaRowerow):
        idWyp = input("Podaj nr rezerwacji.")
        for i in listaWyp:
            if idWyp == i.nrRezerwacji:
                dataOd = stringToDate(i.dataOd)
                dataDo = stringToDate(i.dataDo)
                dateDelta = (dataDo - dataOd).days
                i.czyOddany = '1'
                for j in listaRowerow:
                    if i.nrId == j.nrId:
                        j.dostepnosc = "1"
                        cena = j.cena
        f = open("rowery.txt", "w")

        for i in listaRowerow:
            f.write(i.nrId + ";" + i.kolor + ";" + i.rama + ";" + i.rozmiar + ";" + i.cena + ";" + i.dostepnosc + "\n")

        f.close()

        f1 = open("rent.txt", "w")
        for i in listaWyp:
            f1.write(i.nrRezerwacji + ";" + i.imie + ";" + i.nazwisko + ";" + i.nrId + ";"
                    + i.dataOd + ";" + i.dataDo + ";" + i.czyOddany + "\n")

        f1.close()

        doZaplaty = dateDelta * int(cena)
        print(str(doZaplaty) + 'zl')
        listaWplat = []
        listaWplat.append(doZaplaty)


    def showDebtor(self):
        czasTeraz = datetime.datetime.now()
        dataTeraz = czasTeraz.date()
        rents = getAllRents()
        for i in rents:
            terminOddania = stringToDate(i.dataDo)
            if terminOddania < dataTeraz and i.czyOddany == '0':
                print(i.nrRezerwacji, i.imie, i.nazwisko, i.nrId, i.dataOd, i.dataDo, i.cena)



#get all ma tylko raz pobierac z pliku, po drugim wywolaniu ma juz nie pobierac z pliku


