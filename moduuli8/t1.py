
def hae_kentan_tiedot(icao):
    sql = f"SELECT name FROM airport where ident= '{icao}'"
    print (sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos=kursori.fetchall()