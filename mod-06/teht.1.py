import random

def nopan_silmaluku():
    return random.randint(1,6)

tulos = nopan_silmaluku()
while tulos != 6:
    print("Heitto:", tulos)
    tulos = nopan_silmaluku()
print("Heitto:", tulos)
print("Sait kuutosen!")
