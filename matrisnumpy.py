import numpy as np

matris = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(matris)
print(matris.size) #boyut

print(f"Matrisin ilk elemani : {matris[0,0]}")
 
print(matris[:])

print(matris[::-1])
print("**************")
print(matris[1:])
print(matris[:,1:])

matris = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(matris.shape)

matris2 = matris
print(matris2)
print(matris2[1,1])

matris2[1,1] = 250

print(matris2)


m1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

m2 = m1.copy()
print(m2)
m1[1,1] = 150
print(m1)
print(m2)

m3 = np.arange(0,10,2) #sıfırdan başla 10 a kadar 2'ser arttır
print(m3)

m5= np.random.rand(2,2)
print(m5)

dizi = np.array([[5,15,25],
                 [35,45,55]])

a= np.sum(dizi, axis=1) #axis=1 her satırın toplamıdır
c= np.sum(dizi, axis=0) #axis=0 her kolonun toplamıdır
#5+15+25
#35+45+55
print(a,c)

b = np.prod(dizi) # tüm elemanları çarpar 
print(b)

print(dizi.argmin()) #bir fonksiyonun min noktası 

dizi.clip(2,5) #sadece istenilen iki değer arasındaki değerler kalır
#diğer değerler o değerlere dönüşür.

dizi2 = np.random.rand(3,3)
print(dizi2)
print(dizi2.round())