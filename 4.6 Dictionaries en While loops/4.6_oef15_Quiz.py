import random
quiz = {
    "Wat is de hoofdstad van Frankrijk?": {
        "Opties": ["A. Londen", "B. Parijs", "C. Berlijn", "D. Rome"],
        "Antwoord": "B"
    },
    "Om hoelaat eindigt de schooldag?": {
        "Opties": ["A. 15:30", "B. 16:30", "C. 15:40", "D. 15:00"],
        "Antwoord": "C"
    },
    "Wat is de hoofdstad van Europa?": {
        "Opties": ["A. Brussel", "B. München", "C. Londen", "D. Frankfurt"],
        "Antwoord": "A"
    }
}

doorgaan = "ja"
while doorgaan == "ja":
    vragen = list(quiz.keys()) # Maakt een lijst van de vragen alleen
    random.shuffle(vragen) # Shuffelt de vragen
    print(f"Veel succes! Het aantal vragen van deze quiz is {len(vragen)}.")
    print("Let's go!")
    print("")
    
    score = 0
    index = 0


    while index < len(vragen):
        vraag = vragen[index]
        print(vraag)
        for optie in quiz[vraag]["Opties"]:
            print(optie)
        
        antwoord = input("Geef uw antwoord (A,B,C of D): ").upper().strip()
        if antwoord == quiz[vraag]["Antwoord"]:
            print("Juist!")
            score += 1
            print(f"Jouw score: {score}")
            print(" ")

        else:
            print(f"Helaas, het juiste antwoord was {quiz[vraag]["Antwoord"]}.")
            print(f"Jouw score: {score}")
            print(" ")

        index += 1

    print(f"Einde van de quiz! Jouw totale score is: {score} van de {len(vragen)}.")
    doorgaan = input(f"Wil je de quiz opnieuw spelen? (Ja/Nee): ").lower().strip()

print("Bedankt voor het spelen!")


            



