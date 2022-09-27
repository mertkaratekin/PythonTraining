
#Class
class Arac:
    pass    
     


#instance, object

arac1 = Arac()
arac2 = Arac()
print(type(arac1))
print(arac1,arac2)

class Products:
    pass


p1 = Products() #macbook    
p2 = Products() #iphone     
p3 = Products() #ipad

listProducts = [p1,p2,p3]

for p in listProducts:
    print(p)