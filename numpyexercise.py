import re

data = open("data.txt")
oku = data.read()
print(oku)

mail_listesi = re.findall("\S+@\S+",oku)
print("****************")
print(mail_listesi)

file = open("mailfiltreme.txt","w")
file.write("mail_listesi : ",mail_listesi)
