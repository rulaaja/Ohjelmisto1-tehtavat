class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeus):
        if self.nopeus < self.huippunopeus:
            self.nopeus+=nopeus
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
            print("huippunopeus saavutettu")

    def jarrutus(self):
        for i in range(142):
            self.nopeus -=1
        print("auto jarruttaa")
#(rekisteritunnus ABC-123, huippunopeus 142 km/h)

auto = Auto("ABC-123", 142, 0, 0)

auto.kiihdyta(30)
print(auto.nopeus)

auto.kiihdyta(50)
print(auto.nopeus)

auto.kiihdyta(70)
print(auto.nopeus)

auto.jarrutus()
print(auto.nopeus)



