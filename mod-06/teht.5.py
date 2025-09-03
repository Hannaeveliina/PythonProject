def parittomat_pois(lista):
    uusi_lista=[]
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

alkuperainen = [1,2,3,4,5,6,7,8,9,10]
karsittu = parittomat_pois(alkuperainen)

print("Alkuperäinen lista:", alkuperainen)
print("Karsittu lista (vain parilliset):", karsittu)