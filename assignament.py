values = 1,2,3,4,5

print(type(values))

x, y, *z = values

print(x,y,z)

print(x,y,z[1])