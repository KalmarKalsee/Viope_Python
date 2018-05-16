# -*- coding: cp1252 -*-

tiedosto = str(input("Minkäniminen tiedosto luodaan?: "))
teksti = str(input("Mitä kirjoitetaan tiedostoon?: "))

handle = open(tiedosto, "w")
handle.write(teksti)
handle.close()

print("Luotiin tiedosto",tiedosto,"ja siihen tallennettiin teksti:",teksti)