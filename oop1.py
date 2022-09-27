"""
#Class

class Person:
    #class attributes
    addres = 'no information'
    #constructor (yapıcı method)
    def __init__(self, name, year):  
       
        #object attributes
        self.name = name
        self.year = year

    #instance methods
    def intro(self):
        print('Hello there. I am '+ self.name)
        
    def calculateAge(self):
        return 2022- self.year
    
#instance (object)
p1 = Person(name='ali',year= 1990)
p1.addres = 'Bursa'
p1.intro()
p1.calculateAge()
print(p1)
#accessing object attributes   
print(f"Adim: {p1.name} Dogumyilim : {p1.year} address: {p1.addres} yasim : {p1.calculateAge()}")  
"""
class Circle:
    pi = 3.14 #class attributes
    
    def __init__(self,yaricap =1): #constructor
        self.yaricap = yaricap
        
    def cevre_hesapla(self): #methods
        return 2 * self.pi + self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    
c1 = Circle()  #yaricap default olarak 1 geliyor
c2 = Circle(yaricap=5)


print(f"c1 : alan {c1.alan_hesapla()} cevre : {c1.cevre_hesapla()}")
print(f"c2 : alan {c2.alan_hesapla()} cevre : {c2.cevre_hesapla()}")


