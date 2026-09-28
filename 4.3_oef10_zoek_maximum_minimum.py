import random

lijst = []
for i in range(10):
    lijst.append(random.randint(1,100))

print(f"De lijst is: {lijst}") # controle

max = lijst[0]
min = lijst[0]

for getal in lijst:
    if getal > max:
        max = getal
    if getal < min:
        min = getal
        
print(f"Het maximum is: {max}")
print(f"Het minimum is: {min}")