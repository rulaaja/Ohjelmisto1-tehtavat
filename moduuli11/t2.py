import random

from moduuli9.t4 import voittaja_loytynyt


class Auto:
    aika = 0
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
        Auto.aika += 1

    def kiihdyta(self, nopeus):
        if self.nopeus < self.huippunopeus:
            self.nopeus+=nopeus
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje (self, aika):
        self.matka += self.nopeus * aika

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka, akku):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
        self.akku=akku
        super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)
        Auto.aika += 1

class Polttomoottoriauto(Auto):
        def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka, tankki):
            self.rekisteritunnus = rekisteritunnus
            self.huippunopeus = huippunopeus
            self.nopeus = 0
            self.matka = 0
            self.tankki=tankki
            super().__init__(rekisteritunnus, huippunopeus, nopeus, matka)
            Auto.aika += 1

#Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
#Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
#self, rekisteritunnus, huippunopeus, nopeus, matka, akku
#self, rekisteritunnus, huippunopeus, nopeus, matka, tankki

autot=[]
sahkoauto=Sahkoauto("ABC-15", 180, 100, 0, 52.5)
polttoauto=Polttomoottoriauto("ACD-123", 165, 100, 0, 52.5)

autot.append(sahkoauto)
autot.append(polttoauto)

for tunti in range(3):
    for auto in autot:
        auto.kiihdyta(random.randint(0, 25))
        auto.kulje(1)


for sahkoauto in autot:
    print(f"{sahkoauto.rekisteritunnus}, on kulkenut: {sahkoauto.matka} km")


for polttoauto in autot:
    print(f"{polttoauto.rekisteritunnus}, on kulkenut: {polttoauto.matka} km")



