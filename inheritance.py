# Inheritance (Kalıtım) : miras alma

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")


class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student created")
    # overrride (Method ezme)

    def who_am_i(self):
        print("I am a student")

    def sayHello(self):
        print("Hello I am a student")


class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch
        print("Teacher created")
    def who_am_i(self):
        print("I am a teacher")
        

p1 = Person('Mert', 'Yilmaz')
print(p1.fname, p1.lname)
s1 = Student('Cinar', 'Turan', 1256)
print(s1.fname, s1.lname, s1.studentNumber)
t1 = Teacher("Ebru","Huseyinoglu","English")
print(t1.fname,t1.lname,t1.branch)
p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
t1.who_am_i()