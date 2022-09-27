from unicodedata import name


names = ['Ali','Yagmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

names.append('Cenk')
print(names)
 
names.insert(0,'Sena')
print(names)
"""
del names[-2]
result = names"""
print(names)    
result = 'Ali' in names
print(result)

print(names[::-1])

index = names.index('Deniz')
print(index)

names.sort()
print(names)

years.sort()
print(years)

str = 'Chevrolet,Dacia'
result = str.split(',') #split ayırmak için kullanılır.
print(result)

min = min(years)
max = max(years)
print(min, max)

result = years.count(1998)
print(result)

years.clear()
print(years)
#Kullanıcıdan alacagınız 3 tane marka bilgisini
#bir listede saklayınız.

markalar = []
marka = input("marka: ")
markalar.append(marka)
print(markalar)