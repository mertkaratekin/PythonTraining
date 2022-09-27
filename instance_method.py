class User:
    
    #constructor
    def __init__(self,username,name,surname,birthday):
        #object attribute, instance attribute
        self.username = username
        self.name = name
        self.surname = surname
        self.birthday = birthday
    
    #instance methods
    #objenin methodu
    def info(self):
        return f"{self.username} kullanici adiyla {self.name} {self.surname} sisteme kaydedildi."    
    
    def calculateAge(self):
        yas = 2022 - self.birthday
        return f"{self.username} kullanicinin yasi : {yas}"
u1 = User("Leventrt","Levent","Ertunalilar",1984)
u2 = User("mertrrd","Mert","Karatekin",2002,)

        
print(u1.info(),u1.calculateAge())
print(u2.info(),u2.calculateAge())