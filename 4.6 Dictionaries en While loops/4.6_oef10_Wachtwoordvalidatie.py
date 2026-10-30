speciale_tekens = "!@#$%^&*"

print("Geef een wachtwoord in. Uw wachtwoord moet aan de volgende criteria voldoen:")
print("• Minimaal 8 karakters lang")
print("• Ten minste één hoofdletter")
print("• Ten minste één cijfer")
print("• Ten minste één speciaal karakter (!@#$%^&*)")

while True:
    wachtwoord = str(input("Uw wachtwoord: "))

    lang_genoeg = len(wachtwoord) >= 8

    heeft_hoofdletter = any(teken.isupper() for teken in wachtwoord)
    heeft_cijfer = any(teken.isdigit() for teken in wachtwoord)
    heeft_teken = any(teken in speciale_tekens for teken in wachtwoord)
    
    if lang_genoeg and heeft_hoofdletter and heeft_cijfer and heeft_teken:
        print("Uw wachtwoord is geaccepteerd!")
        break
    else:
        if not lang_genoeg:
            print("Uw wachtwoord is te kort.")
        if not heeft_hoofdletter:
            print("Uw wachtwoord moet minstens één hoofdletter bevatten.")
        if not heeft_cijfer:
            print("Uw wachtwoord moet minstens één cijfer bevatten.")
        if not heeft_teken:
            print(f"Uw wachtwoord moet minstens één speciaal teken ({speciale_tekens}) bevatten.")

        print("Probeer het opnieuw.")






while True:
    wachtwoord = input("Kies een wachtwoord:")

    heeft_hoofdletter = False
    heeft_cijfer = False
    heeft_speciaal = False
    for teken in wachtwoord:
        if teken.isupper():
            heeft_hoofdletter = True
        if teken.isdigit():
            heeft_cijfer = True
        if teken in speciale_tekens:
            heeft_speciaal = True

    if len(wachtwoord) < 8:
        print("Je wachtwoord moet minstens 8 karakters lang zijn.")
    elif not heeft_hoofdletter:
        print("Je wachtwoord moet minstens één hoofdletter bevatten.")
    elif not heeft_cijfer:
        print("Je wachtwoord moet minstens één cijfer bevatten.")
    elif not heeft_speciaal:
        print(f"Je wachtwoord moet minstens één speciaal teken bevatten ({speciale_tekens}).")
    else:
        print("Je wachtwoord is goedgekeurd!")
        break