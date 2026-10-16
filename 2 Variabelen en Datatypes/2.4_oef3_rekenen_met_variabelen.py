oorspronkelijk_bedrag = 50
oorspronkelijk_bedrag = int(oorspronkelijk_bedrag)
boek = 12.50
boek = float(boek)
tijdschrift = 3.75
tijdschrift = float(tijdschrift)
prijs = ((boek * 2) + (tijdschrift * 3))
overschot = oorspronkelijk_bedrag - prijs
print(f"Na het kopen van 2 boeken en 3 tijdschriften heb ik nog €{overschot} over.")