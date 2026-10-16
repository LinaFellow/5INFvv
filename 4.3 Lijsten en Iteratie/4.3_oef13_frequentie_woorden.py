zin = str(input("Geef een zin in: ")) # De wereld is goed en is slecht.
woorden = zin.lower().split() # Zin in losse woorden hakken
print(woorden) 

#Stap 1: unieke lijst maken met alle verschillende woorden
unieke_woorden = []
for woord in woorden:
    if woord not in unieke_woorden:
        unieke_woorden.append(woord) # Dan heb je altijd maar 1 vd woorden erin, geen dubbele

#Stap 2: per uniek woord tellen hoe vaak het voorkomt
for uniekwoord in unieke_woorden:
    teller = 0 # Bij elk nieuw woord vanaf 0 beginnen tellen
    for woord in woorden: # Terug naar gesplitste lowerzin
        if woord == uniekwoord: # Is wereld = de? nee. is wereld = wereld? ja.
            teller = teller + 1
    print(f"{uniekwoord}: {teller}")

