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
