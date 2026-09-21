aankoopbedrag = float(input("Voer het aankoopbedrag in: "))


if aankoopbedrag > 100:
    korting = 0.10
    print("Je krijgt 10% korting.")
    
else: 
    if 50 < aankoopbedrag <= 100:
        korting = 0.05
        print("Je krijgt 5% korting.")
    else:
        korting = 0
        print("Je krijgt geen korting.")

totaalbedrag = aankoopbedrag - (aankoopbedrag * korting)
print(f"De uiteindelijke prijs is: €{totaalbedrag}")