import random
import math

N = input("Kuinka monta pistettä arvotaan? ")

x = y = 0
toistojen_maara = 200000
pareja_arvottu = 0
sisalla = 0


while pareja_arvottu < toistojen_maara:
      x = random.uniform(-1,1)
      y = random.uniform(-1,1)
      pareja_arvottu += 1
      etaisyys = math.pow(x,2) + math.pow(y,2)
      if etaisyys < 1:
          sisalla += 1

simuloitu_pii = 4 * sisalla / toistojen_maara
print(f"Saatu piin likiarvo: {simuloitu_pii:.3f}")

