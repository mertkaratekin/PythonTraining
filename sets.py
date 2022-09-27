fruits = {'orange','apple','banana'}

#print(fruits)

for x in fruits:
    print(x) 
    
fruits.add('cherry')
fruits.update(['mango','grape'])
print(fruits)


myList = [1,2,5,4,4,2,1]
print(set(myList))

fruits.remove('mango')
print(fruits)

fruits.discard('apple')
print(fruits)