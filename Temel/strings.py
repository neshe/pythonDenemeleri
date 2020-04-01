# -*- coding: utf-8 -*-

mesaj = "Merhaba Dünya"

print(mesaj[2:5])

yeniMesaj = mesaj[:5]

print(yeniMesaj)

print(mesaj[len(mesaj)-1:])


#lower - upper

print(mesaj.upper())
print(mesaj.lower())

print(mesaj.replace("ü", "u"))
print(mesaj.replace("a", "z", 2))

bilgi="Engin Demiroğ 33 Ankara"
print(bilgi.split("i")[2])

ad=input("Adınız? ")
print(ad)

sayi1=input("Sayı 1 =? ")
sayi2=input("Sayı 2 =? ")

print (int(sayi1)+int(sayi2))