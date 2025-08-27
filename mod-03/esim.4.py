#Stipendi vai ei?

fys = int(input("Fysiikan pisteet?"))
kem = int(input("Kemian pisteet?"))
mat = int(input("Matikan pisteet?"))

#jos yhdessäkin aineessa pisteet alle 50, niin ei tule stipendiä
if (fys < 50 or kem < 50 or mat < 50):
    print("Sinulle ei voida myöntää stipendiä, ainakin yhdet pisteet alle 50")
elif fys > 90 and mat > 90:
    print("Saat stipendin, matikan ja fysiikan perusteella")
elif kem >  95:
    print("Saat stipendin, kemian pisteiden ansiosta")
else:
    print("Et saa stipendiä, pisteet eivät riitä")