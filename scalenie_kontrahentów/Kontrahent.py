class Kontrahent:
    def __init__(self, id, nazwa, ulica, kod_pocztowy, miejscowosc, kategoria, lat, lng, g_api_adress, g_api_nazwa,
                 org_nazwa, org_ulica, org_kod_pocztowy, org_miejscowosc ):
        self.id = id
        self.nazwa = nazwa
        self.ulica = ulica
        self.kod_pocztowy = kod_pocztowy
        self.miejscowosc = miejscowosc
        self.kategoria = kategoria
        self.lat = lat
        self.lng = lng
        self.g_api_adress = g_api_adress
        self.g_api_nazwa = g_api_nazwa
        self.org_nazwa = org_nazwa
        self.org_ulica = org_ulica

        self.org_kod_pocztowy = org_kod_pocztowy
        self.org_miejscowosc = org_miejscowosc

    def __str__(self):
        return (self.id + " " + self.nazwa + " " + self.ulica + " " + self.kod_pocztowy + " " + self.miejscowosc + " "
                + self.kategoria + " " + self.lat + " " + self.lng + " " + self.g_api_adress + " " + self.org_ulica + " "
                + self.org_kod_pocztowy + " " + self.org_miejscowosc)