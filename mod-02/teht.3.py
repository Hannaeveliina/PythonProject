import math

suorakulmion_kanta = input("Suorakulmion kanta : ")
korkeus = input("Suorakulmion korkeus : ")

suorakulmion_piiri = float(suorakulmion_kanta) * 2 + float(korkeus) *2
suorakulmion_pinta_ala = float(suorakulmion_kanta) * float(korkeus)

print(f"Suorakulmion pinta-ala on {suorakulmion_pinta_ala:.2f}")
print(f"Suorakulmion piiri on {suorakulmion_piiri:.2f}")
