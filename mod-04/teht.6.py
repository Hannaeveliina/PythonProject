import random
N = input("Kuinka monta pistettä arvotaan? ")

if N.isdigit():
    N = int(N)
    n = 0 #Ympyrän sisään osuneet pisteet
    i = 0 # Laskuri, joka laskee montako pistettä on käsitelty

    while i< N:
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        if x**2 + y**2 < 1:
            n += 1
        i += 1 #Seuraava piste

    pii_likiarvo = 4 * n / N
    print(f"Piin likiarvo {N} pisteellä on: {pii_likiarvo}")

elif not N.isdigit():
    print("Virheellinen syöte. Anna kokonaisluku.")

else:
    print("Jotain meni pieleen.")