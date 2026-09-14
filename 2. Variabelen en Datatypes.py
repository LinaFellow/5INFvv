naam = "Lina"
print("Hallo, " + naam)
naam = "Fellow, de hond van Lina"
print("Hallo, " + naam)

leeftijd = 25
print(f"Je bent {leeftijd} jaar oud.")
leeftijd = leeftijd + 1
print(f"Na je verjaardag ben je {leeftijd} jaar oud.")

stad = "Berlijn"
print(f"Mijn favoriete stad is {stad}.")
stad = "Londen"
print(f"Ik wil graag naar {stad}.")

a = 27
b = 43
som = a + b
print(f"De som is {som}.")

teller = 0
teller = teller + 1
print(teller)
teller += 1
print(teller)
# Dit is een comment

x = 5
print(type(x))
y = "Hello"
print(type(y))

tekst = "5ECWI is geweldig"
print(tekst.upper()) # Alles in hoofdletters
print(tekst.lower()) # Alles in kleine letters
print(tekst.replace("geweldig", "fantastisch")) # Vervang een woord

volledige_naam = "Lina Fastré"
print(volledige_naam.upper())
print(volledige_naam.count(''))
print(volledige_naam.replace("Lina", "programmeur"))

leeftijd = 16 # integer
pi = 3.14159 # float

a = 10
b = 3
print(a + b) # Optellen -> Output: 13
print(a - b) # Aftrekken -> Output: 7
print(a * b) # Vermenigvuldigen -> Output: 30
print(a / b) # Delen -> Output: 3.333333333334 (resultaat is altijd een float)
print(a // b) # Gehele deling -> Output: 3 (resultaat is altijd een integer)
print(a % b) # Modulo (rest na deling) -> Output: 1
print(a ** b) # Machtsverheffing -> Output: 1000

import math
pi = math.pi
straal = 7
oppervlakte = (pi * straal * straal)
print(f"De oppervlakte is {oppervlakte}.")

naam = "Lina"
leeftijd = 16
favoriete_vakantiebestemming = "Oostenrijk"
print(f"Mijn naam is {naam}, ik ben {leeftijd} jaar en ik ga graag op vakantie naar {favoriete_vakantiebestemming}.")

is_python_leuk = True
is_programmeren_moeilijk = False
print(type(is_python_leuk)) # Output: <class 'bool'>

x = 5 # Assignment
y = 5 # Assignment
print(x == y) # Vergelijking
print(x != y) # Vergelijking
print(x <= y) 

getal_als_string = "123"
getal = int(getal_als_string)
print(getal + 5) # Output: 128

kommagetal = 3.14159
afgerond_getal = int(kommagetal)
print(afgerond_getal) # Output: 3

leeftijd = 25
leeftijd_als_tekst = str(leeftijd)
print("Ik ben " + leeftijd_als_tekst + " jaar oud.") # Output: Ik ben 25 jaar oud.

naam = input("Wat is je naam? ")
print(f"Hallo, {naam}!")

leeftijd = input("Wat is je leeftijd? ")
leeftijd = int(leeftijd) # Converteren naar een integer
print(f"Volgend jaar ben je {leeftijd + 1} jaar oud.")

getal1 = input("Geef een eerste geheel getal. ")
getal_1 = int(getal1)
getal2 = input("Geef een tweede geheel getal. ")
getal_2 = int(getal2)
som = getal_1 + getal_2
print(f"De som van deze 2 getallen is {som}.")