lentoasemat = {}

def syota_uusi_asema():
    icao = input("Anna lentoaseman ICAO-koodi: ").upper()
    nimi = input("Anna lentoaseman nimi: ")
    lentoasemat[icao] = nimi
    print(f"Lentoasema {icao} tallennettu.")

def hae_asema():
    icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
    if icao in lentoasemat:
        print(f"Lentoaseman nimi: {lentoasemat[icao]}")
    else:
        print("Lentoasemaa ei löytynyt.")

while True:
    print("\nValitse toiminto:")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoasema")
    print("3 - Lopeta")
    valinta = input("Valintasi: ")

    if valinta == "1":
        syota_uusi_asema()
    elif valinta == "2":
        hae_asema()
    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break
    else:
        print("Virheellinen valinta. Yritä uudelleen.")