"""
languages = ["English","Spanish","Turkish","Italian","Chinese"]

def select_language(selection):
    if selection in languages:
        print(f'You selected: {selection}.')
    else:
        print(f'{selection} is not avaible.')
        
selection = input('Please, select a language: ')
select_language(selection)
"""
"""
x = 27.5

if (int(x) == x):
    print(f"{int(x)} is equal to {x}")
else:
    print(f"{int(x)} is not equal to {x}")
"""
"""
list1 = [1,5,7,2,4,12]
result_list = []

def lets_add():
    for i in list1:
        if i % 2 == 0:
            result_list.append(i)
            
lets_add()
print(result_list)
"""
"""
person_list = {
    "omer":25,
    "winston":34,
    "jane":28,
    "robin":47
}
sum = 0

for i in person_list.values():
    if i > 28:
        sum+=i
        
print(sum)
"""
"""
name = "Johnny Doe"

def func():
    global name
    name = "John Doe"
    
func()
print(name)
"""
item_list = ["Laptop", "Headset", "Second Monitor","Mousepad",
"Usb Drive","External Drive"]
item_list.append(["Mouse", "Pencil", "Pen"])
item_list.remove("Mouse")
item_list[0:3]
