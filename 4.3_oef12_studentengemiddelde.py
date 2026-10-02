aantal_studenten = int(input("Hoeveel studenten zijn er? ")) # Grootte lijst bepalen
aantal_studenten_lijst = [aantal_studenten]
namen = [] # [naam1, naam2, naam3,...]
cijfers = [] # [cijfer1, cijfer2, cijfer3,...]

for student in range(1, aantal_studenten + 1):
    naam = str(input(f"Naam van student {student}: "))
    namen.append(naam)
    cijfer = float(input(f"Cijfer van {naam}: "))
    cijfers.append(cijfer)

print(f"Deze studenten zijn er: {namen}")
print(f"Dit zijn de cijfers: {cijfers}")
som = 0

for i in range(0, aantal_studenten):
    cijfer = cijfers[i]
    som = som + cijfer # Moet eerste cijfer zijn uit lijst van cijfers

gemiddelde_cijfer = som / aantal_studenten
print(f"Het gemiddelde cijfer is {gemiddelde_cijfer}.")


for i in range(0, aantal_studenten):
    cijfer = cijfers[i]
    if cijfer > gemiddelde_cijfer:
        print(f"{namen[1]} scoorde boven het gemiddelde.") # nog fout
        




    