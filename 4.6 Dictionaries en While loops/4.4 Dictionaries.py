leeg_woordenboek = {} # Een lege dictionairy

# Een dictionaire met sleutel-waarde paren
student = {
    "naam": "Lina",
    "leeftijd": 16,
    "klas": "5ECWI",
    "vakken": ["Wiskunde", "Informatica", "Nederlands"]
}
print(student["naam"]) # Output: Lina
print(student["leeftijd"]) # Output: 16

# Dit geeft een KeyError als "adres" niet bestaat:
# print(student["adres"])
print(student.get("adres")) # Dit geeft None als "adres" niet bestaat
print(student.get("adres", "Onbekend")) # Dit geeft "Onbekend" als "adres" niet bestaat

#Een nieuwe sleutel-waarde paar toevoegen
student["adres"] = "Overrepen"
#Een bestaande waarde wijzigen
student["leeftijd"] = 17
print(student)

# Verwijderen met del
del student["adres"]
print(student)
# Verwijderen met pop() (geeft de verwijderde waarde terug)
leeftijd = student.pop("leeftijd")
print(f"Verwijderde leeftijd: {leeftijd}")
print(student)

# Itereren over sleutels
for sleutel in student:
    print(sleutel)
# Alternatief: expliciet de keys() methode gebruiken
for sleutel in student.keys():
    print(sleutel)

for waarde in student.values():
    print(waarde)

for sleutel, waarde in student.items():
    print(f"{sleutel}: {waarde}")

scores = {
    "Nederlands": 7,
    "Wiskunde": 8,
    "Engels": 6,
    "Informatica": 9,
    "Geschiedenis": 5
}
# Maak een nieuwe dictionairy met alleen vakken met een voldoende (≥ 6)
voldoendes = {}
for vak, cijfer in scores.items():
    if cijfer >= 6:
        voldoendes[vak] = cijfer
print(voldoendes)

prijzen = {
    "appel": 0.80,
    "banaan": 1.20,
    "sinaasappel": 1.50,
    "kiwi": 2.00
}
# Verhoog alle prijzen met 10%
nieuwe_prijzen = {}
for product, prijs in prijzen.items():
    nieuwe_prijzen[product] = round(prijs * 0.10, 2)
print(nieuwe_prijzen)

school = {
    "5WWI": {
        "klasleraar": "M. Olifant", # Kan ook input zijn
        "lokaal": "B12",
        "studenten": ["Marjan", "Jola", "Nona"]
    },
    "5EWI": {
        "klasleraar": "D. Panter",
        "lokaal": "C03",
        "studenten": ["Eend", "Vogel"]
    },
    "5LWI": {
        "klasleraar": "P. Papegaai",
        "lokaal": "A15",
        "studenten": ["Sebbe"]
    }
}
# Toegang tot geneste waarden
print(school["5WWI"]["klasleraar"]) # Output: M. Olifant
print(school["5EWI"]["studenten"][0]) # Output: Eend

tekst = "dit is een test dit is slechts een test"
woorden = tekst.split()
frequentie = {}
for woord in woorden:
    if woord in frequentie:
        frequentie[woord] += 1
    else:
        frequentie[woord] = 1
print(frequentie)

studenten = [
    {"naam": "Panda", "klas": "5EWI"},
    {"naam": "Jager", "klas": "5WWI"},
    {"naam": "Vlieg", "klas": "5EWI"}
]
per_klas = {}
for student in studenten:
    klas = student["klas"]
    if klas not in per_klas:
        per_klas[klas] = []
    per_klas[klas].append(student["naam"])
print(per_klas)

landcodes = {
    "BE": "België",
    "NL": "Nederland",
    "DE": "Duitsland",
    "FR": "Frankrijk",
    "UK": "Verenigd Koninkrijk"
}
code = input("Voer een landcode in (bv. BE, NL): ")
land = landcodes.get(code, "Onbekende code")
print(f"De landcode {code} staat voor: {land}")