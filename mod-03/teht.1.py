kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä:"))
if kuhan_pituus <= 37:
    print("Kuha on alamittainen, laske kuha takaisin järveen")
if kuhan_pituus > 37:
    print("Kuha on hyvän pituinen")
else:
    vajaus= 37-kuhan_pituus
    print(f"Kuhan sallitusta pyyntimitasta puuttuu {vajaus} senttimetriä")
