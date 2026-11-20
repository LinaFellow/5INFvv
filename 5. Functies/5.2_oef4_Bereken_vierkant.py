def bereken_vierkant(x):
    return x * x

try:
    x = int(input("Geef een getal in: "))
    print(f"Het kwadraat van {x} is {bereken_vierkant(x)}.")

except ValueError:
    print("Ongeldige invoer, geef aub een geheel getal in.")