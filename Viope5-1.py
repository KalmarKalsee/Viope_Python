# -*- coding: cp1252 -*-

tiedosto = open("faktat.txt")
sisalto = tiedosto.read()

print("Tiedostosta luettiin teksti: ",sisalto)

tiedosto.close()