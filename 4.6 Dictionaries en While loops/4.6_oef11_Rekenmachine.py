print("Welkom bij de rekenmachine!")
verderdoen = True

while verderdoen == True:
    try:
        getal_1 = float(input("Voer het eerste getal in: "))
        operator = input("Voer de operator in (+, -, *, /): ").strip()
        getal_2 = float(input("Voer het tweede getal in: "))

    except ValueError:
        print("Ongeldige invoer. Zorg ervoor dat je geldige getallen invoert (gebruik een punt bij kommagetallen).")
        continue

    if operator == "+":
        resultaat = getal_1 + getal_2
        print(f"Resultaat: {getal_1} {operator} {getal_2} = {resultaat}")
    

    elif operator == "-":
        resultaat = getal_1 - getal_2
        print(f"Resultaat: {getal_1} {operator} {getal_2} = {resultaat}")
        

    elif operator == "*":
        resultaat = getal_1 * getal_2
        print(f"Resultaat: {getal_1} {operator} {getal_2} = {resultaat}")
        

    elif operator == "/":
        if getal_2 == 0:
            print("Delen door 0 gaat niet.")
            
    
        else:
            resultaat = getal_1 / getal_2
            print(f"Resultaat: {getal_1} {operator} {getal_2} = {resultaat}")
            

    else: 
        print("Voer een geldige bewerking in. Kies uit (+, -, * of /).")


    ja_of_nee = input("Wil je nog een bewerking invoeren? (ja/nee): ").strip().lower()
    if ja_of_nee == "ja":
        verderdoen = True
    elif ja_of_nee == "nee":
        print("Rekenmachine afgesloten. Fijne dag nog!")
        verderdoen = False
    else:
        print("Je moet ja of nee invoeren.")

