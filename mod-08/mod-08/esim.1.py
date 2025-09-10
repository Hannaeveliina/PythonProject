import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='hanna',
         password='hannevk',
         autocommit=True
         )


def haeLentokentta(koodi):
    sql = f"SELECT * FROM airport WHERE ident = '{koodi}'"
    print(sql)
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

kentta = haeLentokentta('EFHK')
print(kentta['name'], kentta['type'])

