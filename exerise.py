website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan sona Python Programlama Rehberiniz (40 saat)" 

# 1-Course karakter dizisinde kaç karakter bulunmaktadır ?
print(len(course))

# 2- website içinden www karakterini alın.
for harf in website:
    if harf == 'w':
        print(harf)
        
result = website[7:10]
print(result)

# 3- website içinden com karakterini alın.
result = website[22:25]
print(result)
#2.yol
length = len(website)
result = website[length-3:length]
print(result)

# 4- course içinden ilk 15 ve son 15 karakterini alın.
result = course[0:15]
print(result)

result = course[-15:]
print(result)

# 5- course ifadesindeki karakterleri tersten yazdırın.
#result = course[65:0:-1] #baştan başla sona kadar git sonra da tersten yazdir.
result = course[::-1]
print(result)

name, surname, age, job = 'Bora','Yilmaz',32,'muhendis' 
# 6-Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis
print(f"Benim adim {name} {surname}, yasim {age} ve meslegim {job}")

# 7- 'Hello World' ifadesindeki w harfini W ile değiştirin.
 
s= 'Hello world'
s = s[0:6] + 'W'+ s[-4:]
print(s)

m = 'Mert karatekin'
m = m[0:5] + 'K' + m[-8:]
print(m) 

