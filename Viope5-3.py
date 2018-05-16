# -*- coding: cp1252 -*-

tiedosto = open("merkkijonoja.txt")
sisalto = tiedosto.readlines()
tiedosto.close()

for line in sisalto:
	if(line.replace("\n", "").isalnum()):
		print(line, "kelpaa salasanaksi.")
	else:
		print(line, "sisältää virheellisiä merkkejä.")
