"""
ogrenciler = {
    '120' : {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '1234564789'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '123456466789'
    },
    '128': {
        'ad': 'Volkan ',
        'soyad': 'Yukselen',
        'telefon': '123456774789'
    },
}

#1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
#dictionary içinde saklayınız.

#2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini
#gösterin.
"""
ogrenciler = {}

number = input("Ogrenci no : ")
name = input("Ogrenci adı : ")
surname = input("Ogrenci soyad : ")
phone = input("Oğrenci telefon : ")

ogrenciler[number] = {
    'ad' : name,
    'soyad': surname,
    'telefon': phone
}

"""
ogrenciler.update({
    number: {
        'ad':name,
        'soyad': surname,
        'telefon': phone 
    }
})
"""

print(ogrenciler)

ogrNo = input('öğrenci no: ')

print(ogrenciler[number])













