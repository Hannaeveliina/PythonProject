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


h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)
