from BikeRepository import *
from Rent import *
import os
import datetime

def czyRowerJestDostepny(nrId):
    bR = BikeRepository()
    lR = bR.getAll()
    for i in lR:
        if i.nrId == nrId and i.dostepnosc == "dostepny":
            return 1


def getAllRents():
    textFile = open("D:\\Szkolenie\\WypozyczalniaRowerow\\rent.txt", "r")
    calosc = textFile.read()
    a = calosc.splitlines()
    listWyn = []
    for line in a:
        d = line.split(";")
        nrRezerwacji = d[0]
        imie = d[1]
        nazwisko = d[2]
        nrId = d[3]
        dataOd = d[4]
        dataDo = d[5]
        rent = Rent(nrRezerwacji, imie, nazwisko, nrId, dataOd, dataDo)
        listWyn.append(rent)
    textFile.close()
    return listWyn

def getReservationNumber():
    textFile = open("D:\\Szkolenie\\WypozyczalniaRowerow\\rent.txt", "r")

    if os.stat("D:\\Szkolenie\\WypozyczalniaRowerow\\rent.txt").st_size == 0:
        textFile.close()
        return 1


    else:

        tekst = textFile.read()
        linijki = tekst.splitlines()
        for line in linijki:
            w = line.split(";")
            nrRezerwacji = w[0]

        nrRezerwacji = int(nrRezerwacji) + 1

        textFile.close()
        return nrRezerwacji

# def wyszukajWypozyczenie(listaWyp, listaRowerow):
#     idWyp = input("Podaj nr rezerwacji.")
#     for i in listaWyp:
#         if idWyp == i.nrRezerwacji:
#             for j in listaRowerow:
#                 if i.nrId == j.nrId:
#                     j.dostepnosc = "1"
#
#
#
#
#     f = open("D:\\Szkolenie\\WypozyczalniaRowerow\\rowery.txt", "w")
#
#     for i in listaRowerow:
#         f.write(i.nrId + ";" + i.kolor + ";" + i.rama + ";" + i.rozmiar + ";" + i.cena + ";" + i.dostepnosc + "\n")

def stringToDate(dateSting):
    dateObj = datetime.datetime.strptime(dateSting, '%d-%m-%Y')
    dateObj = dateObj.date()
    return dateObj






