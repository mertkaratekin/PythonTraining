#1- Bmw , Mercedes, Opel, Mazda elemanlarına 
#sahip bir liste oluştur.
from turtle import pen


cars = ['Bmw','Mercedes','Opel','Mazda']

#2- Liste kaç elemanlıdır
index =len(cars)
print('Eleman sayisi : ',index)

#3- Lİstenin ilk ve son elemanı nedir.
length = len(cars)
print('Ilk arac:',cars[0] + ' Son arac:',cars[length-1])
#4- Mazda değerini toyota ile değiştirin
cars[-1] = 'Toyota'
result = cars
#5- Mercedes listenin bir elemanı mıdır ?
result = 'Mercedes' in cars
print(result)
#6- Listenin -2. indeksindeki değer nedir?
print(cars[-2])
#7- Listenin ilk 3 elemanını alın
result = cars[0:3]
print(result)
#8 Listenin son iki elemanı yerine Toyota ve
#Renault değerlerini ekleyin.
cars[-2:] = ['Toyota','Renault'] 
print(cars)

#9- Listenin üzerine audi ve nissan değerlerini
#ekleyin
result = cars + ['Audi', 'Nissan']
print(result)
#10- Listenin son elemanını silin
del cars[-1]
result = cars
print(result)
#11- Liste elemanlarını tersten yazdırın
print(len(cars))
result = cars[::-1]
print(result)

 