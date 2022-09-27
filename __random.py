import random

result = random.random() 
result = int(random.uniform(10,100))
result = random.randint(1,1000)

names = ['ali','yagmur','deniz','cenk','ahmet','efe']
result = names[random.randint(0,len(names)-1)]
result = random.choice(names)

print(result)
