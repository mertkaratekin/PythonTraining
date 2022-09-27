from turtle import pensize


website = 'http://www.sadikturan.com'
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
kelime = ' Hello World '
kelime = kelime.strip()
kelime = kelime.lstrip() #soldan olan boşluğu siler.
kelime = kelime.rstrip() #sağdan olan boşluğu siler.
print(kelime)

#2- 'www.sadikturan.com' içindeki  sadikturan bilgisi haricindeki her karakteri silin.

result =website.strip('http://www.com')
print(result)

#3website www ile başlayıp com ile bitiyor mu 

result = website.startswith('www')
print(result)

result = website.endswith('com')
print(result)

#4 'website' içinde '.com' ifadesi var mı ?
result = website.count('.com')
result = website.find('.com')
print(result)


# 5- 'course' içideki kelimelerin hepsi alfabetik sıralı mı
result = course.isalpha()
print(result)

#6 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
kelime = 'Contents'
kelime = kelime.center(50)
print(kelime)
kelime = kelime.replace(' ','*')
print(kelime)

 