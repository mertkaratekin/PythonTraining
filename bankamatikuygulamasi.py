# Bankamatik Uygulaması
from datetime import datetime

MertHesap = {
    'ad': 'Cem Cemil',
    'hesapNo': '1234567',
    'bakiye': 3000,
    'ekhesap': 2000
}
NaciyeHesap = {
    'ad': 'Ali Kara',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekhesap': 1000
}


def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']} ")
    print(f"Hesabınızdaki para : {hesap['bakiye']}")
    print(f"Ekhesaptaki para : {hesap['ekhesap']}")
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Cekim yapabilirsin")
        print(f"kalan para : {hesap['bakiye']}")
    elif (hesap['bakiye'] < miktar):
        
        print("Bakiye yetersiz\nEk hesap kullanmak ister misiniz ")

        cevap = int(input("Evet ise 1 hayır ise 2 yi tusla : "))
        toplam = hesap['bakiye']+hesap['ekhesap']
        if cevap == 1 and (toplam >= miktar):
            print("Ek hesap ile birlikte bakiye yeterli.")
            print("Ek hesaptan cekilen paranin faizi aylik  %5 tir")
            kalan = toplam - miktar
            toplam -= miktar
            ek = miktar - hesap['bakiye']
            print(f"Ekhesaptan kullanılacak tutar: {ek}")
            tarih_string1 = str(input(
                'Ekhesaptan kullandiginiz parayı yatiracaginiz tarihi girin(yyyy-aa-gg): '))
            tarih1 = datetime.strptime(tarih_string1, "%Y-%m-%d")
            print(tarih1)
            tarih_string2 = str(
                input('Ekhesaptan parayı kullandiginiz tarihi girin(yyyy-aa-gg): '))
            tarih2 = datetime.strptime(tarih_string2, "%Y-%m-%d")
            print(tarih2)
            ay = (tarih1-tarih2) / 30
            faizGelecek = hesap['ekhesap'] - kalan
            faiz = ((faizGelecek * 5) / 100)
            print(
                f"Ekhesaptan cekilen {faizGelecek} tl icin uygulanacak faiz: {faiz} tl'dir ")
            total = faizGelecek + faiz
            print(f"{tarih1} Tarihinde odeme yaparsanız borcunuz {total} tl'dir")
            print(f"Ek hesapta kalan para : {kalan}")
            print(f"Sayin {hesap['ad']} bizimle calistiginiz icin tesekkurler...")

        else:
            print(
                f"{hesap['hesapNo']} nolu hesapta {hesap['bakiye']} tl bulunmaktadır.")
            print(f"Sayin {hesap['ad']} bizimle calistiginiz icin tesekkurler...")


paraCek(MertHesap,3750)
