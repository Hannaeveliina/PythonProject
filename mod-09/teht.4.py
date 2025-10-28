import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunnit

autot = []
for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteri, huippunopeus))

kilpailu_kaynnissa = True
tunti = 0

while kilpailu_kaynnissa:
    tunti += 1
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False

autot.sort(key=lambda car: car.kuljettu_matka, reverse = True)

print(f"\nKilpailu päättyi {tunti} tunnin jälkeen!\n")
print("Rekisteri | Huippunopeus | Nopeus | Kuljettu matka")
print("---------------------------------------------------")
for auto in autot:
    print(f"{auto.rekisteritunnus:9} | {auto.huippunopeus:12} | {auto.tämänhetkinen_nopeus:6} | {auto.kuljettu_matka:14.1f}")
