#Rest moet in 2 situaties 0 zijn (door zichzelf en door 0)
#While tot teller gelijk is aan limiet, of For
#Bij elke while moet bibliotheek terug leeg?
#Teller delen door i want oorspronkelijk getal moet hetzelfde blijven

limiet = int(input("Geef een limiet in om priemgetallen te zoeken: "))
teller = 2

priemgetallen = []

while teller <= limiet: #Moet kleiner zijn
    rest_nul = 0 #Reset bij elk getal

    for i in range(1, teller + 1): #Alle getallen testen van 1 tem teller zelf 
        if teller % i == 0:
            rest_nul += 1

    if rest_nul == 2:
        priemgetallen.append(teller)

    teller += 1 #Volgend getal

print(f"Alle priemgetallen tot het limiet van {limiet} zijn: {priemgetallen}")

