#def square(num):
#    return num **2
numbers = [1,3,5,9,8,10]
#map(square, numbers)

result = list(map(lambda num : num ** 2, numbers))
print(result)

#for item in map(square,numbers):
#    print(item)

def checkEven(num):
    return num % 2 == 0
result = list(filter(lambda num : num % 2 == 0, numbers))
print(result)