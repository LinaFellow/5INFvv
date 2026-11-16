import random
lijst = ["appel", "peer", "kiwi"]
geheime_woord = random.choice(lijst)
levens = 6
geraden_letters = []

aantal_streepjes = "_ " * len(geheime_woord)
print(f"Woord: {aantal_streepjes}") # Wordt enkel de eerste keer geprint
print(f"Levens: {levens}")

while levens >= 1:
    gok = input("Raad een letter: ").lower().strip()

    if gok in geheime_woord: # Stap 1 is controleren goed of fout
        print("Goed geraden!")
        if gok not in geraden_letters: # Moet maar 1 keer in die lijst zitten
            geraden_letters.append(gok) 

    else:
        print(f"Helaas, de letter {gok} komt niet voor in het woord.")
        levens -= 1

    weergave = "" # Weergave opbouwen
    for letter in geheime_woord: 
        if letter in geraden_letters: # Terug naar alle geraden letters
            weergave += letter + " "
        else:
            weergave += "_ " # Niet geraden --> blijft een streepje


    print(f"Levens: {levens}")
    print(f"Woord: {weergave}")


    if "_ " not in weergave:
        print("Goed gedaan! Je hebt het woord geraden.")
        break

if levens == 0:
    print("Je bent dood! Je hebt al je levens verloren.")
    print(f"Het geheime woord was {geheime_woord}.")
            





