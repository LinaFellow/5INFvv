lege_lijst = []
cijfers = [1, 2, 3, 4, 5]
lijst_datatypes = [1, "Hallo", True, 3.14, [1, 2, 3]]

eerste_cijfer = cijfers[0] # Geeft 1
derde_cijfer = cijfers[2] # Geeft 3
laatste_cijfer = cijfers[-1] # Geeft 5

cijfers[0] = 10 # Wijzigt het eerste element naar 10
print(cijfers) # Output: [10, 2, 3, 4, 5]

cijfers.append(6) # Nu is cijfers: [10, 2, 3, 4, 5, 6]
cijfers.insert(1,15) # Voegt 15 in op index 1
# Nu is cijfers: [10, 15, 2, 3, 4, 5, 6]

cijfers.remove(15) # Nu is cijfers: [10, 2, 3, 4, 5, 6]

verwijderd_element = cijfers.pop(0)
print(verwijderd_element) # Output: 10
# Nu is cijfers: [2, 3, 4, 5]

cijfers_2 = [7, 23, 3, 100, 29]
lengte = len(cijfers_2) # Output: 5

lijst_1 = [1, 2, 3]
lijst_2 = [4, 5, 6]
lijst_3 = lijst_1 + lijst_2
print(lijst_3) # Output: [1, 2, 3, 4, 5, 6]

genest = [[1, 2], [3, 4], [5, 6]]
print(genest[0]) # Output: [1, 2]
print(genest[0][1]) # Output: 2

cijfers_3 = [1, 2, 3, 4, 5]
for cijfer in cijfers_3:
    print(cijfer)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for rij in matrix:
    for element in rij:
        print(element)

for i in range(5):
    print(i)