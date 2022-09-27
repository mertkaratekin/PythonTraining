from copyreg import add_extension
from unicodedata import name


def changeName(n):
    n = 'ada'
    
name = 'yigit'

changeName(name)
print(name)

def change(n):
    n[0] = 'istanbul'
    
sehirler = ['ankara','izmir']

change(sehirler)
print(sehirler) 

def add(*params):
    return sum((params))

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,30,40,50))



