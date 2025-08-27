laivan_hyttiluokka = input("Anna laivan hyttiluokka (LUX, A, B, C): ")
if laivan_hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella")
elif laivan_hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif laivan_hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif laivan_hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen yläpuolella")
else:
    print("Virheellinen hyttiluokka")