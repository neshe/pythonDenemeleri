# -*- coding: utf-8 -*-

studentsSet={"Engin", "Derin", "Salih", "Ahmet"}

print(studentsSet) #python kendi algoritmasına göre sıralar ve o şekilde sonuç döner

for student in studentsSet:
    print(student)
    
print("derin" in studentsSet)

studentsSet.add("Ali") #ekleme yapılabilir ancak değiştirmenin bir yolu yoktur.

studentsSet.update(["Merve", "Mert", "Selin"]) #birden fazla elemanı tek seferde eklemek gibi düşünülebilir.
print(studentsSet)

#remove bulamayınca hata verir
#discard bulamazsa hata vermez
#studentsSet.pop() son elemanı silmeye yarar

