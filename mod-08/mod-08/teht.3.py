import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='hanna',
         password='hannevk',
         autocommit=True
         )

def hae_koordinaatit(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    return kursori.fetchone()


icao1 = input("Anna ensimmäinen ICAO-koodi: ").upper()
icao2 = input("Anna toinen ICAO-koodi: ").upper()


koord1 = hae_koordinaatit(icao1)
koord2 = hae_koordinaatit(icao2)

if not koord1:
    print(f"Kenttää {icao1} ei löytynyt.")
elif not koord2:
    print(f"Kenttää {icao2} ei löytynyt.")
else:
    etaisyys = geodesic(
        (koord1['latitude_deg'], koord1['longitude_deg']),
        (koord2['latitude_deg'], koord2['longitude_deg'])
    ).kilometers

    print(f"Etäisyys kenttien {icao1} ja {icao2} välillä on noin {etaisyys:.2f} km.")



