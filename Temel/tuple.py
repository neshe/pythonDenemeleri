# -*- coding: utf-8 -*-

tupleListe = (2,4,6, "Ankara")  # oluşturulduktan sonra elemanları değiştirilemez
liste= [2,4,6, "Ankara"]

print(tupleListe)
print(liste)

print(tupleListe[1:2]) #1'den ikiye kadar, 2 dahil değil. dönüş tipi tuple olduğu için (4,) şeklinde çıktı üretir
#atama yaparkende tuple olduğunu anlatabilmek için yine virgül kullanılır verilen değere