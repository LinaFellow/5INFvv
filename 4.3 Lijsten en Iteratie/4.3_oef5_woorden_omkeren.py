woorden = ["Python", "is", "leuk"]

omgekeerde_woorden = []

for woord in woorden:
    omgekeerd = ""
    for letter in woord:
        omgekeerd = letter + omgekeerd
        #omgekeerd1 = P
        #omgekeerd2 = yP
        #omgekeerd3 = tyP

    omgekeerde_woorden.append(omgekeerd)

print(omgekeerde_woorden)