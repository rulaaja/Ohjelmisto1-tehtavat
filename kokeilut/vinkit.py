import random
from tietokanta import laskeLennonPituus,haePelaajanTiedot

def satunnaisuus():
    eka= random.randint(0,2)
    return eka



def faktoja():
    faktat = ("Saastutit tällä lennolla: haePelaajanTiedot ",
              "Lentoyhtiöt käyttävät edelleen pääasiassa kerosiinia, fossiilista polttoainetta. ",
              "Helsinki–New York (noin 6 700 km) tuottaa noin 1 500–2 000 kg CO₂ per matkustaja.",


    valittu_fakta = faktat[satunnaisuus()]
    print(f"Tässä hauska fakta: {valittu_fakta}")

faktoja()

