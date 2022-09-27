
from unicodedata import name


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        print("Product nesnesi olusturuldu.")
        
p1 = Product('Mercedes A','500000')
p2 = Product("BMW 320",'300000')
p3 = Product("Renault","200000")

print(p1.name,p1.price,
      p2.name,p2.price,
      p3.name,p3.price)
