luvut = []

syote = input("Anna luku: ")
while syote !="":
    luku = float(syote)
    luvut.append(luku)
    syote = input("Anna luku: ")


luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
print(luvut[:5])