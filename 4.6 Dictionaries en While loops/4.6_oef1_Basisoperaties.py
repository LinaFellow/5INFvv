persoon = {
    "naam": "Lina",
    "leeftijd": 16,
    "school": "Van Veldeke",
    "hobby's": ["lopen", "paardrijden"]
}
# 1. Waarde van sleutel naam printen
print(persoon["naam"])

# 2. Nieuwe sleutel toevoegen
persoon["woonplaats"] = "Overrepen"

# 3. Ouder worden
persoon["leeftijd"] = persoon["leeftijd"] + 1 # of persoon["leeftijd"] += 1

# 4. Sleutel school verwijderen
del persoon["school"]

# 5. Eindresultaat
print(persoon)