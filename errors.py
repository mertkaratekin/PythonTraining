#error => hata

#error handling => hata yönetimi

#print(a) => nameerror

#print(10/0) => Zerodivisionerror

"""try: 
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('y icin 0 girilemez')
except ValueError:
    print('x ve y icin sayisal eger girin')"""
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except:
        print("Hatali bilgi girdiniz ")
    else:
        break 
    finally:
        print('tyr except sonlandı.')