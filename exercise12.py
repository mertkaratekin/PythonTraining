"""
#1 gönderilen kelimeyi belirtilen kez ekranda yazan fonksiyon

def tekrarYaz(kelime, kere):
    while kere > 0:
        print(kelime)
        kere -= 1
        
tekrarYaz('Mert',10)
    
#Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon.

def listeCevir(*params):
    liste = []
    
    for param in params:
        liste.append(param)
        
    return liste
    
result = listeCevir(10,20,30,40,50,60,70,'Merhaba')
print(result)
"""
# Gönderilen iki sayının arasındaki tüm asal sayıları bul
"""
def asalBul(num1, num2):
    for sayi in range(num1,num2+1):
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                    print(sayi)
asalBul(2, 8)
"""
