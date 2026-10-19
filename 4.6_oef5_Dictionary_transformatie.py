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

#2 Enkel producten duurder dan €1.50 (originele prijzen)
duurder = {}

#3 Producten in hooofdletters
hoofdletters = {}