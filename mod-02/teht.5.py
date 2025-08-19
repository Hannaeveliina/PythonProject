leiviskat = float(input("Anna leiviskät : "))
naulat = float(input("Anna naulat : "))
luodit = float(input("Anna luodit : "))

#Yksi leiviska = 20 naulaa
#Yksi naula = 32 luotia
#Yksi luoti = 13.3 grammaa

luotien_maara = leiviskat*20*32+ naulat*32 + luodit
grammat_yhteensa = (luotien_maara*13.3)

kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000
print("Massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
