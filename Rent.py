


class Rent:
    def __init__(self,nrRezerwacji ,imie, nazwisko, nrId, dataOd, dataDo, cena, czyOddany):
        self.nrRezerwacji = nrRezerwacji
        self.imie = imie
        self.nazwisko = nazwisko
        self.nrId = nrId
        self.dataOd = dataOd
        self.dataDo = dataDo
        self.cena = cena
        self.czyOddany = czyOddany

    def rentABike(self):
        f = open("rent.txt", "a")
        f.write(str(self.nrRezerwacji) + ";" + self.imie + ";" + self.nazwisko + ";" + self.nrId + ";"
                + self.dataOd + ";" + self.dataDo + ";" + self.cena + ";" + self.czyOddany + "\n")
        self.nrRezerwacji += 1
        f.close()

    def getAllRents(self):
        textFile = open("rent.txt", "r")
        calosc = textFile.read()
        a = calosc.splitlines()
        for line in a:
            d = line.split(";")
            nrRezerwacji = d[0]
            imie = d[1]
            nazwisko = d[2]
            nrId = d[3]
            dataOd = d[4]
            dataDo = d[5]
            czyOddany = d[6]
            rent = Rent(nrRezerwacji, imie, nazwisko, nrId, dataOd, dataDo, czyOddany)
        textFile.close()
        return rent
