# -*- coding: cp1252 -*-

n = int(input("Kuinka monta kierrosta?: "))

tulos = 0
for i in range(0, n):
    tulos = tulos+i
    #print(tulos)

print("Kertymäksi saatiin:",tulos)