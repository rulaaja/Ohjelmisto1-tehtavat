class Auto:

    aika = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
        Auto.aika+= 1.5

    def kulje (self, aika):
        self.matka += self.nopeus * aika
        print(f"auton matka on nyt {self.matka}")

#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.


auto = Auto("ABC-123", 142, 60, 2000)

auto.kulje(1.5)

print(
    f"Auton rekisteritunnus on {auto.rekisteritunnus} , auton huippunopeus on {auto.huippunopeus}, auton nopeus hätäjarrutuksen jälkeen on "
    f"{auto.nopeus}  ja auton kokonaismatka on {float(auto.matka)}.")