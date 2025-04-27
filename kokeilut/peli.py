import mysql.connector



def hae_lentokenttia(icao):
    sql=f"select airport.name,airport.type, airport.ident from airport where iso_country ='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokenttien lukumäärä: {rivi[1],rivi[0]}.")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Apinamies88!',
         autocommit=True
         )

icao=input("MAAKOODI:")
hae_lentokenttia(icao)