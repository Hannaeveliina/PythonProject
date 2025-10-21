class Auto:
    def __init__(self, rekisteritunnus, huippunopeus,):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto.rekisteritunnus}")
print(f"Auton huippunopeus: {auto.huippunopeus} km/h")
print(f"Auton tämänhetkinen nopeus: {auto.tämänhetkinen_nopeus} km/h")
print(f"Autolla kuljettu matka: {auto.kuljettu_matka} km")