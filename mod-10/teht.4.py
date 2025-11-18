import random
from tabulate import tabulate

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        self.autot.sort(key=lambda car: car.kuljettu_matka, reverse=True)
        tulostettavat = []
        for auto in self.autot:
                tulostettavat.append([auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka])

        print(tabulate(tulostettavat,["Rekisteritunnus", "Huippunopeus", "Nopeus", "Matka"]))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = [Auto(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    tunti += 1
    kilpailu.tunti_kuluu()

    if tunti % 10 == 0:
        print(f"\n--- Tilanne {tunti}. tunnin jälkeen ---")
        kilpailu.tulosta_tilanne()


print(f"\n--- Kilpailu päättyi {tunti}. tunnin jälkeen ---")
kilpailu.tulosta_tilanne()
