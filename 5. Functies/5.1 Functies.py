def groet():
    print("Welkom bij functietjes")
groet() #Roep de functie aan (kan meerdere keren)

def groet_persoon(naam): # 'naam' is een parameter
  print(f"Hallo, {naam}!")
groet_persoon("Fellow") # "Fellow" is een argument

def tel_op(getal1, getal2):
  som = getal1 + getal2
  print(f"De som van {getal1} en {getal2} is {som}")
tel_op(5, 3)
tel_op(10, -2)

def optelling(getal1, getal2):
  som = getal1 + getal2
  return som # Geef de berekende som terug
resultaat = optelling(10, 5) # Vang de return waarde op in een variabele
print(f"Het resultaat is: {resultaat}")
print(f"Nog een berekening: {optelling(1, 2)}") # Gebruik de return waarde direct

globale_var = "Ik ben globaal"

def mijn_functie():
  lokale_var = "Ik ben lokaal"
  print(lokale_var)
  print(globale_var) # Globale variabelen zijn wel toegankelijk binnen functies
mijn_functie()
print(globale_var)

def tel_op(getal1, getal2):
  """
  Deze functie telt twee getallen bij elkaar op.

  Args:
    getal1: Het eerste getal.
    getal2: Het tweede getal.

  Returns:
    De som van getal1 en getal2.
  """
  som = getal1 + getal2
  return som
# Met help() toon je de docstring van een functie
help(tel_op)