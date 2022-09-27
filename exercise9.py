"""
sayilar = [1,3,5,7,9,12,19,21]
x = 0
while x < 8:
    print(sayilar[x])
    x+=1

bas = int(input("baslangıc degeri giriniz: "))
bit = int(input("bitis degeri giriniz: "))

for sayi in sayilar:
    if (bas < sayi < bit):
        print(sayi)
"""
"""
sayi = 100
while sayi >= 1:
    print(sayi)
    sayi -= 1
"""
sayilar = []
x = 0
while x < 5:
    sayi = int(input("Sayi giriniz: "))
    x += 1
    sayilar.append(sayi)
    sayilar.sort()
    
print(sayilar)