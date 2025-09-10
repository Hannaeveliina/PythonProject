luvut = []
arvo = int(input("Anna kokonaisluku, 0 = lopetus:"))
while arvo != 0:
    luvut.append(arvo)
    arvo = int(input("Anna kokonaisluku, 0 = lopetus:"))

luvut_joukko = set(luvut)
print("Kaikki antamasi eri arvot, kukin näytetään vain kerran")
print(luvut_joukko)

print("Kaikki luvut allekkain")
for alkio in luvut_joukko:
    print(alkio)

lista = list(luvut_joukko)
lista.sort(reverse = True)
print("Antamasi luvut suurimmasta pienimpään")
for alkio in lista:
    print(alkio)