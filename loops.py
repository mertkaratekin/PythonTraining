"""
d = {'k1':1, 'k2': 2, 'k3': 3}

for key,value in d.items():
    print(key,value)
"""
"""
sayilar = [1,3,5,7,9,12,19,21]
for sayi in sayilar:
    if sayi % 3 == 0:
        print(f"{sayi} : 3'un katidir.")
    else:
        print("3'un kati degil")
"""
"""
sehirler = ['kocaeli', 'istanbul','ankara','izmir','rize']

for sehir in sehirler:
    if len(sehir) <= 5:
        print(sehir)
"""
urunler = [
    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s6', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '3000'},
    {'name': 'samsung s10', 'price': '7000'}
]
toplam = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam += fiyat
    
print(toplam)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    