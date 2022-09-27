class Person:
    def __init__(self, name, year):
        self.year = year
        if len(name) > 5:
            raise Exception("En fazla 4 karakter")
        else:
            self.name = name
    def bilgi_goster(self):
        print(f"{self.name} isimli kisi {2022 - self.year} yasindadir")

        
p1 = Person("Ali", 1989)
p1.bilgi_goster()
