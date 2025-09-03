def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat: ")
    for tavara in tavarat:
        print("- " + tavara)
    return

reppu = ["Vesipullo", "Kartta", "Kompassi"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)