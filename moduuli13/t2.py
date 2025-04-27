import mysql.connector
from flask import Flask, request

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Apinamies88!',
         autocommit=True
         )
app = Flask(__name__)
@app.route('/summa')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

def hae_lentokenttia(icao):
    sql=f"select airport.name, airport.ident from airport where airport.ident ='{icao}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"LENTOKENTTÄ {rivi[0]}.")
    return



icao=input("ANNA ICAO KOODI: ")
hae_lentokenttia(icao)