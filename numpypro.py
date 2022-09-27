import numpy as np

dizi = np.arange(5)

print(dizi)

dizi2 = np.array([[0,1, 2, 3, 4,5]])

print(dizi2)

print(dizi2.shape)

#transpoz alma
matris = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(matris.T)

matris2 = np.array([[10,20,30],
                  [40,50,60],
                  [70,80,90]])

matris3 = np.concatenate((matris,matris2)) #birleştirme
print(matris3)
"""
axis=0 satırlar üzerinden işlem yapar.
axis=1 sütunlar üzerinden işlem yapar.
vstack = matrisi dikey birleştirir.
hstack = matrisi yatay birleştirir.
"""

a= np.linspace(0,10,5) # sıfırdan başlar ona kadar eşit aralıklarla beş farklı sayı üretir.
print(a)
