def laske_summa(lista):
    summa = 0
    for luku in lista:
        summa += luku
    return summa

luvut = [2, 17, 6, 9, 10]
summan_tulos = laske_summa(luvut)

print("Listan luvut", luvut)
print("Listan lukujen summa on:", summan_tulos)