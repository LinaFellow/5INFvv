import random
getal = random.randint(1,100)

print("Raad het getal tussen 1 en 100!")
print("Als je wilt stoppen, geef dan de letter 'q' als getal in.")


aantal_gokken = 0

while True:
    jouwgetal = (input("Jouw getal: "))

    if jouwgetal.lower() == "q":
            print(f"Jammer! Het getal dat je moest raden was {getal}.")
            break
    
    jouwgetal = int(jouwgetal)
    aantal_gokken += 1

    if jouwgetal > getal:
        print("Dat getal is te hoog!")

    elif jouwgetal < getal:
        print("Dat getal is te laag!")

    elif jouwgetal == getal:
        print(f"Goed geraden! Je hebt het getal {getal} gevonden na {aantal_gokken} keer proberen.")
        break

