import random
toistot = 0
heitot_yhteensa = 0
while toistot < 100000:

    noppa1 = noppa2 = heitot = 0
    while (noppa1!=6 or noppa2!=6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    toistot = toistot + 1
    heitot_yhteensa = heitot_yhteensa + heitot
heitot_keskimaarin = heitot_yhteensa/toistot
print(f"Heitot keskimäärin: {heitot_keskimaarin:6.2f}")

