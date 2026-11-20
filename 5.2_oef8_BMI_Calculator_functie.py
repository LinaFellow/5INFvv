def bereken_bmi(gewicht, lengte):
    bmi = gewicht / (lengte * lengte)
    return bmi

try:
    gewicht = float(input("Wat is je gewicht in kg?: "))
    lengte = float(input("Wat is je lengte in meter?: "))
    print(f"Jouw bmi is {bereken_bmi(gewicht, lengte):.1f}")

except ValueError:
    print("Ongeldige invoer. Schrijf kommagetallen met een punt.")