class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,tämänhetkinen_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinen_nopeus += nopeuden_muutos

        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunnit

auto = Auto("ABC-123", 142, 60, 2000)

print(f"Ajonopeus: {auto.tämänhetkinen_nopeus} km/h")

auto.kulje(1.5)

print(f"Autolla kuljettu matka yhteensä: {auto.kuljettu_matka} km")
