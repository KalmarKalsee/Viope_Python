# -*- coding: cp1252 -*-

jatkumo = True
while jatkumo:
    syote = input("Kirjoita jotain: ")
    if syote == "lopeta":
        print("Lopetit ohjelman.")
        jatkumo = False
    else:
        print(syote)