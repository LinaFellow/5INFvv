# Vaste wisselkoers: 1 EUR = 1.15 USD op 18/09/2026
WISSELKOERS_EUR_NAAR_USD = 1.15

bedrag = float(input("Bedrag: "))
bronvaluta = input("Bronvaluta (EUR of USD): ").strip().upper() # strip is alles omzetten naar kleine letters (geen gekke tekentjes)

if bronvaluta == "EUR": 
    doelvaluta = "USD"
    resultaat = bedrag * WISSELKOERS_EUR_NAAR_USD
if bronvaluta == "USD": # of elif
    doelvaluta = "EUR"
    resultaat = bedrag / WISSELKOERS_EUR_NAAR_USD

print(f"{bedrag} {bronvaluta} is gelijk aan {resultaat:.2f} {doelvaluta}") # Belangrijk om de print naar links te zetten
