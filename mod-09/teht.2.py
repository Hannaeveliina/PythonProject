class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,):
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

auto = Auto("ABC-123", 142)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(f"Auton nopeus kiihdytysten jälkeen: {auto.tämänhetkinen_nopeus} km/h")

auto.kiihdytä(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto.tämänhetkinen_nopeus} km/h")