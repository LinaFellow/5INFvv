def vind_maximum(lijst):
    maximum = lijst[0]
    for i in lijst:
        if i > maximum:
            maximum = i
    return maximum

lijst = [3, 6, 9, 10, 0, 1, 2, 4]
print(f"Het maximum in de lijst {lijst} is {vind_maximum(lijst)}.")