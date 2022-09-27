#####range
for item in range(2,10):
    print(item)
#####enumerate
#index = 0
greeting = 'Hello There'

for item in enumerate(greeting):
    print(item)
    #print(f'index : {index}, letter : {letter} ')
    #index += 1 
    
#####zip

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

print(list(zip(list1, list2)))

for item in zip(list1, list2):
    print(item)



