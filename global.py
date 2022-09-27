x = 'global x'

def function():
    x = 'local x'
    print(x)
    
function()
print(x)


name = 'Cinar'

def changeName(new_name):
    name = new_name
    print(name)
    
changeName('Mert')
print(name)