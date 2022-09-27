urunler = []
num = int(input("Kac kayit yapılacak : "))
i = 0
while i < num:
    name = input("Urun adi giriniz : ")
    price = int(input("Urun fiyatı giriniz: "))
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1
for urun in urunler:
    print(f'urun adi : {urun["name"]}, fiyati : {urun["price"]}')