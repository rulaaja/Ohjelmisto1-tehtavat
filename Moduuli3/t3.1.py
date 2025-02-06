pituus = float(input("Anna kuhan pituus : "))
if pituus>=37:
    print("Kuha on täysimittainen.")
if pituus<=36:
    alimitta=abs((pituus)-37)

    print(f"Kuha on alimittainen, sallitusta pituudesta puuttuu: {alimitta}" )