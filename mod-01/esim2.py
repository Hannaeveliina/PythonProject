banaanit = input("Anna banaanien määrä (kg): ")
omenat = input("Anna omenoiden määrä (kg): ")
appelsiinit = input("Anna appelsiinien määrä (kg): ")

banaani_kilohinta = 2.85
omena_kilohinta = 3.15
appelsiini_kilohinta = 4.05

banaani_hinta = float(banaanit) + banaani_kilohinta
omena_hinta = float(omenat) + omena_kilohinta
appelsiini_hinta = float(appelsiinit) + appelsiini_kilohinta

print("Ostosten yhteenveto: ")
print(f"Banaanin hinta on {banaani_hinta:.2f}")
print(f"Omenan hinta on {omena_hinta:.2f}")
print(f"Appelsiinin hinta on {appelsiini_hinta:.2f}")
