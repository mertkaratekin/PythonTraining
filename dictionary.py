#key - value

# 41 => kocaeli
"""
sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

print(plakalar[sehirler.index('kocaeli')])
print(plakalar[sehirler.index('istanbul')])

#print(plakalar['kocaeli']) => 41

plakalar = { 'kocaeli' : 41, 'istanbul' : 34}
print(plakalar['kocaeli'])

plakalar['ankara'] = 6
plakalar['kocaeli'] = 'new value'

print(plakalar)
"""
users = {
    'sadikturan': {
        'age' : 36,
        'roles': ['admin','users'],
        'email': 'sadikturan@gmail.com',
        'addres': 'kocaeli',
        'phone' :'123456789'
    },
    'cinarturan': 2
}
print(users['sadikturan']['age'])
print(users['sadikturan']['email'])
print(users['sadikturan']['addres'])
print(users['sadikturan']['roles'][0])

print(users['sadikturan'])


