# fonksiyondan geriye fonksiyon döndürme
"""
def usalma(number):
    def inner(power):
        return number ** power

    return inner


two = usalma(2)
three = usalma(3)
print(two(3))
print(three(4))
"""


def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolunun {1} numarali sayfasina ulasabilir". format(role, page)
        else:
            return "{0} rolunun {1} numarali sayfasina ulasamaz". format(role, page)
    return inner
user1 = yetki_sorgula("Admin Page")
print(user1("Admin"))