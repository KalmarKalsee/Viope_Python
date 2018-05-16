# -*- coding: cp1252 -*-

name = input("Anna nimi: ")

if name == "Erkki":
	pwd = input("Anna salasana: ")
	if(pwd == "Esimerkki"):
		print("Salasana ja nimi oli oikein!")
	else:
		print("Salasana oli väärin.")
else:
	print("Nimi oli väärin.")