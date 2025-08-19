import math

ympyran_sade = input("Syötä ympyrän säde : ")
nelion_sivun_pituus = input("Syötä neliön sivun pituus : ")

ympyra_ala = math.pi * float(ympyran_sade) **2
nelio_ala = float(nelion_sivun_pituus)**2
print(f"Ympyrän pinta-ala on {ympyra_ala:.2f}")
print(f"Neliön pinta-ala on {nelio_ala:.2f}")
