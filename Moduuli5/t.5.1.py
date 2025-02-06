import random

arpakuutiot = []
tulos=0

luku = int(input("Monta arpakuutiota sinulla on, lopeta painamalla Enter: "))

for arpa in range(luku):
    arpakuutiot.append(random.randint(1,6))

for arpa in arpakuutiot:
    tulos += arpa

print (f"Arpakuutioiden summa on {tulos}!")
