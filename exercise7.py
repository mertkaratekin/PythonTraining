"""
name = input("İsim giriniz:" )
age = int(input("yasinizi giriniz: "))
grade = input("egitim durumu : ")

if age >= 18 and ((grade == 'lise') or (grade == 'uni')):
    print(f"{name} ehliyet alabilirsiniz .")
else:
    print("Ehliyet alamazsiniz")
    
"""
"""
exam1 = int(input("1. sinav notunu giriniz :"))
exam2 = int(input("2. sinav notunu giriniz :"))
exam3 = int(input("1. sözlü notunu giriniz :"))

avg = (exam1 + exam2 + exam3)/3
if  (85<= avg <100):
    print(5)
elif (avg >= 70):
    print(4)
"""
import datetime
tarih = input('araciniz hangi tarihte trafige citki (2019/8/9)')
tarih = tarih.split('/')
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days
 
if days<=365:
     print("1.servis araligi ")
elif days > 365 and days<=365*2:
     print("2.servis aralıgı")
elif days>365*2 and days<=365*3:
    print("3.servis aralıgı")
else:
    print("hatalı süre ")
     





