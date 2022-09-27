numbers = [x for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x % 3 == 0]
print(numbers)

myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)