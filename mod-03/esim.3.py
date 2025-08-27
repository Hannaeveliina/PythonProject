#Sähkölasku

kulutus = float(input("Kuinka monta kWh sähköä kului?"))
if kulutus <=50 and kulutus >=0:
    hinta = kulutus*0.10
elif kulutus <=200:
    hintaA = 50 * 0.10              #50 eka kWh:n hinta
    yli50 = kulutus - 50           #kuinka paljon kulutus yli 50kWh?
    hintaB = yli50 *0.08           #sähkön hinta yli 50 kWh osalta
    hinta = hintaA + hintaB        # loppuhinta
elif kulutus > 200:
    hintaA = 50 * 0.10             # 50 eka kWh:n hinta
    hintaB = 150 * 0.08            # sähkön hinta 50-200 kWh välillä
    yli200 = kulutus - 200
    hintaC = yli200 * 0.06         # sähkön hinta yli 200 kWh:n osalta
    hinta = hintaA + hintaB + hintaC
else: #jos käyttäjä antanut negatiivisen luvun
    print("Kulutuksen täytyy olla positiivinen luku")

print(f"Sähkön kulutuksesi maksaa {hinta:.2f} euroa")