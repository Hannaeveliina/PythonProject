import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='hanna',
         password='hannevk',
         autocommit=True
         )

def hae_lentokentat_maassa(maakoodi):
    sql = """
        SELECT type, COUNT(*) AS maara
        FROM airport
        WHERE iso_country = %s
        GROUP BY type
    """
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (maakoodi,))
    tulokset = kursori.fetchall()
    return tulokset

maakoodi = input("Anna maakoodi: ").upper()
kentat = hae_lentokentat_maassa(maakoodi)

if kentat:
    print(f"\nLentokenttien lukumäärät maassa {maakoodi}:")
    for kentta in kentat:
        print(f"{kentta['type'].replace('_', ' ').capitalize()}: {kentta['maara']} kpl")
else:
    print("Lentokenttiä ei löytynyt annetulla maakoodilla.")