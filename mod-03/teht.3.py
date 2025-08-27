sukupuoli= input("Anna biologinen sukupuoli (nainen/mies): ")
hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo g/l: "))

if sukupuoli == "nainen":
    if hemoglobiiniarvo < 117:
       print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo <=175:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo <=195:
        print("Hemoglobiiniarvo on normaali")
    else:
        print("Hemoglobiiniarvo on korkea")

else:
    print("Virheellinen sukupuoli")



