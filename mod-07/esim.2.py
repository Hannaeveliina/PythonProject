hedelmat = {}

for nro in range(3):
    avain = input("Anna hedelmän nimi: ")
    arvo = int(input("Kuinka monta kiloa? "))
    hedelmat[avain] = arvo
print("Antamasi tiedot sanakirjassa:")
print(hedelmat)