hoogte = int(input("Wat is de hoogte van de rechthoek? "))
breedte = int(input("Wat is de breedte van de rechthoek? "))

for rij in range(hoogte):
    regel = ""

    for kolom in range(breedte):
        regel = regel + "*"

    print(regel)