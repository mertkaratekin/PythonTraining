#bellekte yer işgal etmeyen iterator olusturur.

from email import generator


def cube():
    for i in range(5):
        yield i**3 # yieldin olusturdugu değer saklanmaz böylece bellek tasarrufu sağlanır.
#Olusturulan eleman anlık olarak kullanılıp çöp olacaksa yani 
#tekrar çağırılmayacaksa generator kullanılır. Eğer saklanacaksa
#iterator kullanılır.     
for i in cube():
    print(i)

generator = (i**3 for i in range(5))
print(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


liste = [i**3 for i in range(5)]
print(liste)