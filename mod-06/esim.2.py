def long_names(animals):
    pitkat_nimet = []
    for animal in animals:
        if len(animal) > 5:
            pitkat_nimet.append(animal)
    return pitkat_nimet

elukat = ["kissa", "koira", "elefantti", "leijona", "kirahvi"]
paivitetyt_elukat = long_names(elukat)
print(elukat)
print(paivitetyt_elukat)