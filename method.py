#method 
"""
 
myString = 'Hello'

a = myString.upper()
print(a)
"""
"""

#METHODS
def sayHello(name = 'user'):
    print('Hello '+ name)
    
sayHello('Mert') 
sayHello()
"""
from turtle import pensize

"""
def sayHello(name = 'user'):
    return 'Hello '+ name
    
msg =sayHello('Mert') 
print(msg)

def total(num1,num2):
    return num1 + num2

result = total(10,20)
print(result)
"""
def yasHesapla(dogumYili):
    return 2022 - dogumYili 

ageMert = yasHesapla(2002)
print('Yasiniz: ',ageMert)

def Emeklilik(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    
    if emeklilik > 0:
        print(f'emekliliginize {emeklilik} yil kaldi')
    else:
        print(f"Bitti")
        
Emeklilik(1969, 'Mert')