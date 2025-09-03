import random
lukumaara = []

luku = int(input("Kuinka monta arpakuutiota haluat heittää?"))
summa = 0
kertaa = 0

for i in range(luku):
    silmaluku = random.randint(1,6)
    summa += silmaluku
    lukumaara.append(silmaluku)
    kertaa = kertaa + 1

print(lukumaara)
print(summa)



