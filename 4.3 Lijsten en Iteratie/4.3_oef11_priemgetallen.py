priemgetallen = []

for getal in range(1,51): #beginnen met 1 #daarna 2
    aantal_delers = 0
    for deler in range(1,getal+1): # bepaald hoeveel keer het gaat delen
        if getal % deler == 0: # rest is nul --> is dus een deler #2/1 --> 0 #2/2 --> 0
            aantal_delers = aantal_delers + 1 # aantal delers is 1 #aantald = 1 #aantald = 2
    if aantal_delers == 2:
        priemgetallen.append(getal)

print(f"Priemgetallen tussen 1 en 50: {priemgetallen}")
