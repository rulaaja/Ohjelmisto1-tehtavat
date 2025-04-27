class Henkilo:
    def __init__(self, nimi, sukunimi):
        self.nimi = nimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.nimi} {self.sukunimi}")



class Kirja(Henkilo):
    def __init__(self, nimi, sukunimi, kirja, sivumaara, kirjailija):
        super().__init__(nimi, sukunimi)
        self.kirja = kirja
        self.sivumaara = sivumaara
        self.kirjailija = kirjailija

    def tulosta_sivumaara(self):
        print(f"{self.sivumaara}")


class Lehti(Henkilo):
    def __init__(self, nimi, sukunimi, lehti, paatoimittaja):
        super().__init__(nimi, sukunimi)
        self.lehti = lehti
        self.paatoimittaja = paatoimittaja



aku = Lehti("Aki", "Hyyppä", "Aku Ankka", "Aki Hyyppä")
rosa = Kirja("Rosa", "Liksom", "Hytti n:o 6", 200, "Rosa Liksom")
aku.tulosta_tiedot()
rosa.tulosta_tiedot()
rosa.tulosta_sivumaara()