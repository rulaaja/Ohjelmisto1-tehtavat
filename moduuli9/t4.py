import random

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


autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i}", random.randint(100, 200),0,0))

    voittaja_loytynyt = False;

    while not voittaja_loytynyt:
        for auto in autot:
            auto.kiihdyta(random.randint(-10, 25))
            auto.kulje(1)
        if auto.matka >= 10000:
            voittaja_loytynyt = True
            break

autot.sort(key=lambda a: a.matka, reverse=True)
for auto in autot:
    print(f"{auto.rekisteritunnus}, {auto.huippunopeus}, {auto.nopeus}, {auto.matka}")

