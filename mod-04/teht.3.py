luvut = []
syote = input("Anna luku: ")

while syote != "":
    luku = float(syote)
    luvut.append(luku)
    syote = input("Anna luku: ")

if luvut:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et syöttänyt lukua.")