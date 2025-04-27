
nimet = set()




while True:
    nimi = input("Anna nimi (Syötä tyhjämerkkijono lopettaaksesi): ")
    if nimi == "":
        break
    if nimi not in nimet:
        nimet.add(nimi)
        nimi = input("Uusi nimi: ")
        if nimi == "":
            break
    if nimi in nimet:
        nimi=input("Aiemmin syötetty nimi: ")
        if nimi == "":
            break
    if nimi not in nimet and nimi !="":
        nimet.add(nimi)
        if nimi == "":
            break

for n in nimet:
    print(f"Nimet: {[n]}")

