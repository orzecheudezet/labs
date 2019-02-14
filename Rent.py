


class Rent:
    def __init__(self,nrRezerwacji ,imie, nazwisko, nrId, dataOd, dataDo):
        self.nrRezerwacji = nrRezerwacji
        self.imie = imie
        self.nazwisko = nazwisko
        self.nrId = nrId
        self.dataOd = dataOd
        self.dataDo = dataDo

    def rentABike(self):
        f = open("D:\\Szkolenie\\WypozyczalniaRowerow\\rent.txt", "a")
        f.write(str(self.nrRezerwacji) + ";" + self.imie + ";" + self.nazwisko + ";" + self.nrId + ";"
                + self.dataOd + ";" + self.dataDo + "\n")
        self.nrRezerwacji += 1
        f.close()

    def getAllRents(self):
        textFile = open("D:\\Szkolenie\\WypozyczalniaRowerow\\rent.txt", "r")
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
            rent = Rent(nrRezerwacji, imie, nazwisko, nrId, dataOd, dataDo)
        textFile.close()
        return rent
