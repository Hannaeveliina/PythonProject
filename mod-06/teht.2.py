import random

def nopan_silmaluku():
    return random.randint(1,tahkoja)

tahkoja = int(input("Anna nopan tahkojen määrä: "))
maksimi = tahkoja

tulos = nopan_silmaluku()
while tulos != maksimi:
    print("Heitto:", tulos)
    tulos = nopan_silmaluku()
print("Heitto:", tulos)
print("Sait maksimin!")