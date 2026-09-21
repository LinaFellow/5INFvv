gewicht = input("Wat is je gewicht?: ")
gewicht = float(gewicht)
lengte = input("Wat is je lengte in meter?: ")
lengte = float(lengte)

bmi = gewicht / (lengte * lengte)

print(f"Je BMI is {bmi:.1f}")