# -*- coding: cp1252 -*-

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))

valinta = int(input("(1) +\n(2) -\n(3) *\n(4) /\nTee valinta (1-4): "))

if valinta == 1:
    print("Tulos on:",luku1+luku2)
elif valinta == 2:
    print("Tulos on:",luku1-luku2)
elif valinta == 3:
    print("Tulos on:",luku1*luku2)
elif valinta == 4:
    print("Tulos on:",luku1/luku2)
else:
    print("Valintaa ei tunnistettu.")