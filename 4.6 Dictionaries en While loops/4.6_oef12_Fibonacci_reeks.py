while True:
    try:
        limiet = int(input("Voer een limiet voor de Fibonacci-reeks in: "))
        break #While-loop stopt en gaat verder naar de volgende while
                   
    except ValueError:
        print("Ongeldige invoer. Voer aub een geheel getal in!")

fibonacci_reeks = []
a = 0
b = 1

while a <= limiet: 
    fibonacci_reeks.append(a)
    a, b = b, a + b #a wordt b en b wordt a + b
        
print(f"De Fibonacci-reeks tot {limiet} is: {fibonacci_reeks}")



