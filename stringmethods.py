from email import message
from email.errors import MessageParseError


message = ' Hello There. My name is Mert Karatekin'

#message = message.upper() komple büyük harfe çevirir
#message = message.lower() komple küçük harfe çevirir
#message = message.title() #her kelimenin baş harfini büyük yazdırır.
#message = message.capitalize() cümlenin sadece ilk harfini büyük yazar.
#message = message.strip() #eğer stringin başında boşluk varsa boşluğu kaldırır.
#message = message.split('.') noktalardan ayırır stringi
#message = message.split(' ') #ayırma işlemi yapar.
#message =  '*'.join(message)#birleştirme işlemi yapar

#message = message.replace('Mert','Naciye')#yer değiştirme işlemi yapar.
#index =message.find("Mert")
#print(index)

message = message.center(50)
print(message)



