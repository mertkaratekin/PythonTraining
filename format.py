from unittest import result


name = 'Mert'
surname = 'Karatekin'
age = 20

print('My name is {}'.format(name))

result = 20 / 70

print("The result is : {} ".format(result))

print("The result is : {:1.3} ".format(result))
#Yazılan 1 kaç boşluk bırakılacağını belirler.
#yuvarlama işlemi için kullanılır ve virgülden sonraki kısımın basamak sayısını belirler

print(f"My name is {name} {surname} I'm {age} years old.")
#fstring  string ifadenin başına f ekleyip format methodundan 
#kurtulmak için kullanılır.


































































