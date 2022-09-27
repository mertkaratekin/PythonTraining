from operator import length_hint


name = 'Mert'
surname = 'Karatekin'
age = 20

greeting = 'My name is ' + name + ' ' + surname + ' and I am '+ str(age) + ' years old'
length = len(greeting)

print(greeting)
print(greeting[0])
print(length)
print(greeting[length-1])
print(greeting[-1]) #dizinin son elemanını yazdırır.

print(greeting[2:5]) #ikinci karakterden beşinci karaktere yazdırır.

print(greeting[3:]) #üçten başlar sona kadar gider.
print(greeting[2:40:2])