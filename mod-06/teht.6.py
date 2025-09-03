import math

def lasketaan_hinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    hinta = hinta_euro / pinta_ala_m2
    return hinta

print("Anna ensimmäisen pizzan tiedot:")
halkaisija1 = float(input("Halkaisija (cm):"))
hinta1 = float(input("Hinta (€): "))

print("Anna toisen pizzan tiedot:")
halkaisija2 = float(input("Halkaisija (cm): "))
hinta2 = float(input("Hinta (€): "))

hinta1 = lasketaan_hinta(halkaisija1, hinta1)
hinta2 = lasketaan_hinta(halkaisija2, hinta2)
print(f"Ensimmäisen pizzan yksikköhinta: {hinta1:.2f} €/m2")
print(f"Toisen pizzan yksikköhinta: {hinta2:.2f} €/m2")

if hinta1 < hinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif  hinta2 < hinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmilla pizzoilla on sama yksikköhinta.")