woordenboek = {
    "hallo": {"Engels": "hello", "Frans": "bonjour", "Duits": "hallo"},
    "wereld": {"Engels": "world", "Frans": "monde", "Duits": "welt"},
    "hond": {"Engels": "dog", "Frans": "chien", "Duits": "hund"},
    "paard": {"Engels": "horse", "Frans": "cheval", "Duits": "pferd"},
}

Nederlands_woord = input("Geef mij een Nederlands woord: ").lower().strip()
doeltaal = input("Naar welke taal wilt u dit woord vertalen? (Engels, Frans of Duits): ").strip().capitalize()

if Nederlands_woord in woordenboek.keys():
    if doeltaal in woordenboek[Nederlands_woord]:
        vertaling = (woordenboek[Nederlands_woord][doeltaal])
        print(f"De vertaling van '{Nederlands_woord}' naar het {doeltaal}: {vertaling}")
    else: print("Je moet een ander woordenboek zoeken, dit woordenboek vertaalt enkel naar het Engels, Frans of Duits.")
    

if Nederlands_woord not in woordenboek.keys():
    print("Dit woord staat niet in het woordenboek.")
