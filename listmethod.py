numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
print(val)

val = max(letters)
print(val)

val = numbers[3:6]
print(val)

numbers[4] = 40

numbers.append(49)
print(numbers)

numbers.insert(3,78) #3. indexin hemen sonuna ekler 
print(numbers)

#numbers.pop() #en sondan eleman siler.
#numbers.pop(1) # birinci elemanı siler.
numbers.remove(49) # silmek istenilen elemanı gir.
numbers.sort() #sıralanır

numbers.reverse() #listeyi tam tersine çevirir

print(numbers)