class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

#(rekisteritunnus ABC-123, huippunopeus 142 km/h)


auto = Auto("ABC-123", 142)


print(f"Auton rekisteritunnus on {auto.rekisteritunnus} , auton huippunopeus on "
      f"{auto.huippunopeus}, auton nopeus nyt on {auto.nopeus}  ja auton kokonaismatka on {auto.matka}.")