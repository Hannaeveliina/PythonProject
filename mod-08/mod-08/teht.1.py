import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='hanna',
         password='hannevk',
         autocommit=True
         )

def hae_lentoasema(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    return tulos

# Kysy käyttäjältä ICAO-koodi
icao = input("Anna lentoaseman ICAO-koodi: ").upper()
kentta = hae_lentoasema(icao)

if kentta:
    print(f"Lentoaseman nimi: {kentta['name']}")
    print(f"Sijaintikunta: {kentta['municipality']}")
else:
    print("Lentoasemaa ei löytynyt.")