#error handling
import re


liste = ["1","2","5a","10b","abc","10","50"]

#liste elemanları arasında sayısal degerleri bulun.

for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue
    
