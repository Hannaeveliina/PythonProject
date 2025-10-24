class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeus):
        # asetetaan haluttu nopeus, ei yli huippunopeuden eikä alle 0
        if nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


sahkoauto = Sähköauto("ABC-15", 180, 52.5)
bensaauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sahkoauto.kiihdytä(120)
bensaauto.kiihdytä(150)

sahkoauto.kulje(3)
bensaauto.kulje(3)

print(f"Sähköauto {sahkoauto.rekisteritunnus}: {sahkoauto.kuljettu_matka} km")
print(f"Polttomoottoriauto {bensaauto.rekisteritunnus}: {bensaauto.kuljettu_matka} km")
