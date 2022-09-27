"""try:
    file = open("newfile.txt","r")
except:
    print("Hata")
finally:
    print("Dosya kapandi")
    file.close()"""

file = open("newfile.txt","r",encoding='utf-8')
"""
#for ile 
for i in file:
    print(i,end="")
"""
"""
#read fonk. ile
content = file.read()
print(content)
"""
"""
content = file.read(5)
content = file.read(3)

print(content)
"""
"""
#file.readline() # Her seferinde bir satır okur.

print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")

"""
liste = file.readlines()
print(liste)


file.close()
