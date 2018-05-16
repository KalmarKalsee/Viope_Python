# -*- coding: cp1252 -*-

FILE_NAME = "muistio.txt"


while True:

    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta")
    valinta = int(input("Mitä haluat tehdä?: "))

    if valinta == 1:
        handle = open("muistio.txt")
        content = handle.read()
        print(content)
        
    elif valinta == 2:
        handle = open(FILE_NAME,"a")
        teksti = input("Kirjoita uusi merkintä: ")
        handle.write(teksti + "\n")
        handle.close()
    
    elif valinta == 3:
        handle = open("muistio.txt","w")
        handle.close()
        print("Muistio tyhjennetty.")
    
    elif valinta == 4:
        print("Lopetetaan.")
        break

else:
    print("Tuntematon valinta.")