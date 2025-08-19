import random

kolmenumeroinen_koodi = ""
for _ in range(3):
     numero = random.randint(0,9)
     kolmenumeroinen_koodi += str(numero)

nelinumeroinen_koodi = ""
for _ in range(4):
      numero = random.randint(1,6)
      nelinumeroinen_koodi += str(numero)

print("Kolmenumeroisen lukon koodi:" , kolmenumeroinen_koodi)
print("Nelinumeroisen lukon koodi:" , nelinumeroinen_koodi)

