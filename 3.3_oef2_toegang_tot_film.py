Leeftijd = int(input("Wat is je leeftijd: "))

if Leeftijd >= 16:
    print("Welkom, je mag naar de film!")
elif Leeftijd < 16:
    Volwassene = input("Is er een volwassen begeleider bij? (JA/NEE): ").strip().lower()
    if Volwassene == "ja":
        print("Welkom, je mag samen naar de film!")
    else: print("Sorry, je mag helaas niet naar de film.")