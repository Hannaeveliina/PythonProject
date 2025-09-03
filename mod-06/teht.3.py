def gallona_litra(gallona):
    return gallona * 3.785

while True:
    syote = float(input("Anna bensiinin määrä gallonoina (neg. lopettaa): "))
    if syote < 0:
        print("Muunnos lopetettu")
        break
    litrat = gallona_litra(syote)
    print(f"{syote} gallonaa on {litrat:.3f} litraa.")