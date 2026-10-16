telefoonboek = {}
afgesloten = False
keuze = "0"
# Een for lus in plaats van een while-lus:
# Het menu wordt maximaal 1000 keer getoond
for beurt in range(1000):
    if not afgesloten:
        print()
        print("Telefoonboek menu:")
        print("1. Contact toevoegen")
        print("2. Contact opzoeken")
        print("3. Contact verwijderen")
        print("4. Alle contacten weergeven")
        print("5. Afsluiten")
        keuze = input("Kies een optie van 1 tot en met 5: ")
        print()

        if keuze == "1": 
            naam = input("Naam: ") # quinn
            naam.lower()
            if naam in telefoonboek:
                print("Dit contact bestaat al.")
            else:
                nummer = input("Telefoonnummer: ") #string, geen integer want anders 0 niet erbijgeteld)
                telefoonboek[naam] = nummer
                # Quinn: 0474839567
                # Fenne: 0485599090
                print("Contact toegevoegd!")
            

        elif keuze == "2": # Gewone if zou ook kunnen
            contact = input("Welk contact wilt u opzoeken? ")
            contact.lower()
            if contact in telefoonboek:
                print(f"Het telefoonnummer van {contact} is: {telefoonboek[contact]}")
            else:
                print("Contact niet gevonden.")

        elif keuze == "3":
            variabele = input("Welk contact wilt u verwijderen? ")
            variabele.lower()
            if variabele in telefoonboek:
                del telefoonboek[variabele]
                print(f"{variabele} is uit het telefoonboek gegooid.")
            else:
                print("Dit contact staat niet in het telefoonboek.")

        elif keuze == "4":
            if len(telefoonboek) == 0:
                print("Het telefoonboek is nog leeg.")
            else:
                print("Alle contacten in uw telefoonboek:")
                for naam, nummer in telefoonboek.items():
                    print(f"{naam}: {nummer}")

        elif keuze == "5":
            afgesloten = True # De volgende ronde doet niets meer.
            print("Tot ziens :)")

        else:
            print("Je hebt een ongeldige keuze ingegeven. Voer a.u.b. een keuze in van 1 t.e.m. 5 in.")

