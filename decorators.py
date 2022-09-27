"""
def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan once islemler")
        func(name)
        print("fonksiyondan sonraki islemler")
    return wrapper

@my_decorator #bunu ekledikten sonra atama yapmaya gerek yoktur.
def sayHello(name):
    print("hello",name)
    
def sayGreeting():
    print("greeting")
    
#sayHello = my_decorator(sayHello) #@my_decorator yazmak yeterli
sayHello("Ali")
#sayGreeting = my_decorator(sayGreeting)
#sayGreeting()
"""
import math
import time


def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " + str(finish - start) + " saniye surdu")
    return inner
 
@calculate_time
def usalma(a, b):
    print(math.pow(a, b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))


usalma(2, 3)
faktoriyel(3)
