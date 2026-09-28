getallen = []
aantal = int(input("Hoeveel getallen wil je invoeren? "))
som = 0

for i in range(1, aantal + 1):
    getal = float(input(f"Voer getal {i} in: "))
    getallen.append(getal)

for cijfer in getallen:
    som += cijfer
    gemiddelde = som / aantal

print(f"Het gemiddelde is: {gemiddelde}.")