cars = {}

number = input('Arabanın nosu :')
mark = input("Arabanın markası : ")
modal = input("Arabanın modeli: ")
price = input("arabanın fiyatı: ")

cars[number] = {
    'marka' : mark,
    'model' : modal,
    'fiyat' : price
}

print(cars)

CarNo = input("Arac numarası giriniz :")
print(cars[CarNo])

print("Aranılan aracın numarası : ",number,"markası :",mark,"modeli : ",modal,"fiyatı : ", price)