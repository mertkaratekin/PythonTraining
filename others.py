#Identity Operator : is

from re import X


x = y = [1,2,3]
z= [1,2,3]

print(x == y) 
print( x is y) #x ve y aynı reference tutuyor
print(x is z)  #x ve z aynı reference tutmuyor


#Membership Operator : in 

x = ['apple','banana']
print('banana' in x)

