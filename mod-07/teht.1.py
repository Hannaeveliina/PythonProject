talvi = (12,1,2)
kevät = (3,4,5)
kesä = (6,7,8)
syksy = (9,10,11)

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if kuukausi in talvi:
    print("Vuodenaika on talvi.")
elif kuukausi in kevät:
    print("Vuodenaika on kevät")
elif kuukausi in kesä:
    print("Vuodenaika on kesä")
elif kuukausi in syksy:
    print("Vuodenaika on syksy")
else:
    print("virheellinen kuukauden numero")
