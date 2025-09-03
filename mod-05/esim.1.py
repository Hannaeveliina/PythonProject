#Tee ohjelma, joka kysyy käyttäjältä lukuja, kunnes käyttäjä antaa negatiivisen luvun.
#Luvut talletetaan listaan, viimeistä eli negatiivista lukua ei kuitenkaan talleteta listaan.
#Järjestä luvut suuruusjärjestykseen, pienin ensin. Tulosta sen jälkeen listan kaikki luvut.
#Tarkista sen jälkeen, onko luku 10 mukana listassa.
luvut = []
arvo = int(input("Anna kokonaisluku, negatiivinen arvo lopettaa: "))
while arvo >= 0:
    luvut.append(arvo)
    arvo = int(input("Anna kokonaisluku, negatiivinen arvo lopettaa: "))
    luvut.sort()
    print(luvut)
#onko arvo 10 listassa? käyetään true/false toimintoa
loytyi = 10 in luvut
if loytyi:
    print("Arvo 10 löytyi")
else:
    print("Arvoa 10 ei löytynyt")