aantal_studenten = int(input("Hoeveel studenten zijn er? "))
aantal_studenten_lijst = [aantal_studenten]
print(aantal_studenten_lijst)

for student in aantal_studenten_lijst:
    naam = str(input(f"Naam van student {student}: "))
    cijfer = float(input(f"Cijfer van {naam}: "))
