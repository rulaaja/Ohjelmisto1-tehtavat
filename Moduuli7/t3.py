icao = {}

def lasku()
    nimi = input("Haluatko syöttää uuden lentoaseman: ")
    while nimi != "" and nimi not in nimet:
        nimet.add(nimi)
        nimi2 = input("Uusi nimi: ")
        if nimi2 in nimet:
            nimi2 = input("Aiemmin syötetty nimi: ")
        if nimi2 == "" and nimi2 not in nimet:
            break
        if nimi2 not in nimet:
            nimet.add(nimi2)
        if nimi2 or nimi=""
            break
        else:
            input("Aiemmin syötetty nimi: ")