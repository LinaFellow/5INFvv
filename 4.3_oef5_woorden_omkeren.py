woorden = ["Python", "is", "leuk"]

omgekeerde_woorden = []

for woord in woorden:
    omgekeerd = ""
    for letter in woord:
        omgekeerd = letter + omgekeerd

    omgekeerde_woorden.append(omgekeerd)

print(omgekeerde_woorden)