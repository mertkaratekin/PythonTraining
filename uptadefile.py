 #with open("newfile.txt","r+",encoding='utf-8') as file:
#    print(file.read())
    
#with open("newfile.txt","r+",encoding='utf-8') as file:
#    file.seek(20)
#    file.write ("deneme") #güncelleme yapar.
    

#****Sayfa sonunda guncelleme****#
""" 
#with open("newfile.txt","r+",encoding='utf-8') as file:
#    print(file.read()) 

with open("newfile.txt","a",encoding='utf-8') as file:
    file.write("\nMeliha Karatekin")
    
with open("newfile.txt","r+",encoding='utf-8') as file:
    print(file.read()) 
""" 
###***Sayfa başında güncelleme***### 
"""
with open("newfile.txt","r+",encoding='utf-8') as file:
    content = file.read()
    content = "Efe Turan\n" + content  
    file.seek(0)
    file.write(content)

with open("newfile.txt","r",encoding='utf-8') as file:
    print(file.read())
"""
   
###***Sayfa ortasında güncelleme***### 

with open("newfile.txt","r+",encoding='utf-8') as file:
    list = file.readlines()
    list.insert(2,"Ali Korkmaz\n")
    file.seek(0)
    for i in list:
        file.write(i)

with open("newfile.txt","r",encoding='utf-8') as file:
    print(file.read())