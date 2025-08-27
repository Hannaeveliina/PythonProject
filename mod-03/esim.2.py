ika = int(input("Paljonko on ikää?"))
if ika >=18:
    print("Olet täysi-ikäinen. Tervetuloa äänestämään")
else:
    vajaus=18 - ika
    print(f"Et ole täysi-ikäinen. Voit äänestää {vajaus} vuoden kuluttua")

print("Hyvää päivänjatkoa!")