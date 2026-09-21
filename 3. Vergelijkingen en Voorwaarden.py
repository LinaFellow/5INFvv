print(2 > 1.09)      # True
print(10 >= 10.0)    # True
print(-1 < 0)        # True

leeftijd = 16
heeft_toestemming = True

print(leeftijd >= 16 and heeft_toestemming)    # True
print(leeftijd < 16 or heeft_toestemming)      # True
print(not heeft_toestemming)                   # False

x = 7
print(x > 0 and x < 10)   # True (x ligt tussen 0 en 10)
print(x < 0 and x < 10)   # False (x is niet kleiner dan 0)

leeftijd = 16
lengte = 163

print(leeftijd >= 18 or lengte >= 160)    # True (lang genoeg)
print(leeftijd >= 18 or lengte >= 170)    # False (niet oud en niet lang genoeg)

# Test 1: Getallen
a = 10
b = 5
c = 10.0
print(a == c)    # Ik denk True
print(a > b)     # True

# Test 2: combinaties
x = 7
print(x > 5 and x < 10)   # True
print(x < 5 or x > 8)     # False

leeftijd = 16

if leeftijd >= 16:
    print("Je mag een bromfiets besturen!")

leeftijd_2 = 15

if leeftijd_2 >= 16:
    print("Je mag een bromfiets besturen!")

else:
    print("Je moet nog even wachten met bromfietsen.")

leeftijd_3 = 17
heeft_rijbewijs = False

if leeftijd_3 >= 18:
    if heeft_rijbewijs:
        print("Je mag autorijden!")
    else:
        print("Je moet eerst je rijbewijs halen.")

else:
    print("Je moet nog wachten tot je 18 jaar bent.")

leeftijd_4 = 19
heeft_ticket = True
heeft_id = True

if leeftijd_4 >= 18 and heeft_ticket and heeft_id:
    print("Welkom bij het evenement!")
else:
    print("Je hebt geen toegang.")

leeftijd = int(input("Wat is jouw leeftijd? "))
lengte = int(input("Wat is jouw lengte in cm? "))

if leeftijd >= 12 and lengte >= 150:
    print("Stap maar in!")
else:
    print("Sorry, je mag niet in de attractie.")