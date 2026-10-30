producten = {
    "appel": 0.75,
    "banaan": 1.20,
    "sinaasappel": 1.50,
    "kiwi": 2.00,
    "druiven": 2.50,
    "mango": 1.95,
    "ananas": 3.25
}

#1 Alle prijzen + 5%
verhoogd = {}
for sleutel, prijs in producten.items(): 
    inflatie = round(prijs * 1.05, 2)
    verhoogd[sleutel] = inflatie

print(f"De verhoogde prijzen:")
for sleutel, waarde in verhoogd.items():
    print(f"{sleutel}: €{waarde}")

#2 Enkel producten duurder dan €1.50 (originele prijzen)
duurder = {}
for sleutel, prijs in producten.items():
    if prijs > 1.50:
        duurder[sleutel] = prijs

print("De producten die duurder zijn dan €1.50:")
for sleutel, waarde in duurder.items():
    print(f"{sleutel}: €{waarde:.2f}")

#3 Producten in hooofdletters
hoofdletters = {}
for sleutel, waarde in producten.items():
    hoofdletters[sleutel.upper()] = waarde

print("Alle sleutels in hoofdletters:")
for sleutel, waarde in hoofdletters.items():
    print(f"{sleutel}: €{waarde}")