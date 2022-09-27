import numpy as np
liste = [1,2,3]

liste2 = np.array(liste)
liste2 += 1
print(liste2)  

liste = [1,2,3,"4"]
dizi = np.array(liste)
print(dizi)
print(type(dizi))

print(dizi.shape) # dizinin genel boyutunu verir.(4,0),(2,2) etc.
print(dizi.ndim) #dizinin satir olarak boyutunu verir.

liste2 = ([1,2],[3,4])
print(liste2,)
print(type(liste2))

dizi2= np.array(liste2)
print(dizi2)

print(dizi2.shape) # dizinin genel boyutunu verir.(4,0),(2,2) etc.
print(dizi2.ndim) #dizinin satir olarak boyutunu verir.

dizi2.fill(6) #tüm elemanları istenilen rakamla değiştirir.
print(dizi2)