cijfers = {
    "Nederlands": 7,
    "Engels": 6,
    "Wiskunde": 8,
    "Informatica": 9,
    "Geschiedenis": 5,
    "Aardrijkskunde": 7,
    "Biologie": 6
}

som = 0
som = sum(cijfers.values())
print(f"Test: de som van de dictionary is: {som}")
aantal_cijfers = len(cijfers)
print(f"Test: het aantal opgetelde cijfers is: {aantal_cijfers}")
gemiddelde_cijfer = som / aantal_cijfers # Gewone deling / geeft een float

print(f"1. Het gemiddelde cijfer is {gemiddelde_cijfer:.1f}.") # Afronden op 1 decimaal

hoogste_cijfer = 0
bijbehorend_vak = ""
for vak, elkcijfer in cijfers.items(): # Zowel de sleutels als de waarde afgaan :)
    if elkcijfer > hoogste_cijfer:
        hoogste_cijfer = elkcijfer
        bijbehorend_vak = vak

print(f"2. Het hoogste cijfer is {hoogste_cijfer}. Dit cijfer haalde je voor het vak {bijbehorend_vak}.")

laagste_cijfer = list(cijfers.values())[0] # Of de eerste waarde uit de dictionary nemen
slechte_vak = ""
for vak, cijfer in cijfers.items(): # Sleutels + waardes!
    if cijfer < laagste_cijfer:
        laagste_cijfer = cijfer
        slechte_vak = vak

print(f"3. Het laagste cijfer is {laagste_cijfer}. Dit cijfer haalde je voor het vak {slechte_vak}.")


print(f"4. Alle vakken met een voldoende:")
for vak, cijfer in cijfers.items(): 
    if cijfer >= 6:
        print(f"• {vak}")

print()
print(f"5. Alle vakken met een onvoldoende:")
for vak, cijfer in cijfers.items(): 
    if cijfer < 6:
        print(f"• {vak}")



    


