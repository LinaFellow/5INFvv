import random

Getal = random.randint(1,10)
Raad_getal = int(input("Raad het geheime getal tussen 1 en 10: "))

if Getal == Raad_getal:
    print("Gefeliciteerd, je hebt het goed geraden!")

else:
    print("Helaas, dat is niet correct. Probeer het nog eens.")