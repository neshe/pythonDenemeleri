# -*- coding: utf-8 -*-

sozluk = {
    "book" : "kitap",
    "table" : "masa"
    }

print(sozluk)

print(sozluk["book"])

sozluk["book"]="kitap1"
print(sozluk["book"])
sozluk["pencil"]="kalem"

del(sozluk["book"])
print(sozluk)