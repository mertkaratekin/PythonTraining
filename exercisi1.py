from ast import arg


def displayUser(**args): 
    #Dictionary göndermek istiyorsan çift yıldız
    #Liste, tuple göndermek istiyorsan tek yıldız
    #TYPE IS DICTIONARYB
    for key, value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name = 'Cinar', age = 2, city = 'istanbul')
displayUser(name = 'Ada', age = 12, city = 'kocaeli',phone = '1233')
displayUser(name = 'Yigit', age = 14, city = 'ankara',phone = '2334',email = 'yigit@gmail.com')


def myFunc(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
myFunc(10,20,30,40,50, key1 = 'value 1', key2 = 'value 2')
