# ogrenci1 = "Engin"
# ogrenci2 = "Mehmet"
# ogrenci3 = "Salih"

# print(ogrenci1)
# print(ogrenci2)
# print(ogrenci3)

ogrenciListesi = ["Engin", "Mehmet", "Salih"]

print(ogrenciListesi[0])
print(ogrenciListesi[1])
print(ogrenciListesi[2])

ogrenciListesi.append("Ahmet")
ogrenciListesi.remove("Salih")
print(ogrenciListesi)

#list constructer
sehirler=list(("Ankara", "İstanbul"))
print(sehirler)
print(len(sehirler))

#diger fonksiyonlar

#print(sehirler.clear()) #bu fonksiyon kalıcı etki bırakır. içi boşalır.

print(sehirler.count("Ankara")) #listenin içindeki ankara ifadesinin sayısı
print("Ankara indexi ="+ str(sehirler.index("Ankara")))  #Ankara kaçıncı indexte? ilk bulduğunda bitirir.

sehirler.pop(1) #indeksi 1 olanı çıkar
sehirler.insert(0,"İstanbul")
print(sehirler)
sehirler.reverse()
print(sehirler)

sehirler2=sehirler #diziler referans tiptir. dolayısıyla atama değil referans geçirme olur.

print(sehirler2)

sehirler2[0]="İzmir"
print(sehirler)
print(sehirler2)


sehirler3=sehirler.copy() #kopyasını al

sehirler.extend(sehirler3)
print(sehirler)

sehirler.sort()
sehirler.reverse()
print(sehirler)