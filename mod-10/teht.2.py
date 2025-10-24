class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen_kerros = alin  # Hissi alkaa alimmasta kerroksesta

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa!")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa!")

    def siirry_kerrokseen(self, kerros):
        print(f"Siirretään hissi kerrokseen {kerros}...")
        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_numero, kohdekerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"\nAjetaan hissiä {hissi_numero + 1} kerrokseen {kohdekerros}:")
            self.hissit[hissi_numero].siirry_kerrokseen(kohdekerros)


taloni = Talo(1, 10, 3)

taloni.aja_hissiä(0, 7)

taloni.aja_hissiä(1, 3)

taloni.aja_hissiä(2, 10)

taloni.aja_hissiä(0, 1)
