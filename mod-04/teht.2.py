muuntaja = 2.54
tuumat = float(input("Anna tuumamäärä :"))

while tuumat >= 0:
    sentit = tuumat*muuntaja
    print(f"{tuumat} tuumaa on {sentit:.2f} cm")

    tuumat = float(input("Anna tuumamäärä: "))

print("Ohjelma lopetettu")