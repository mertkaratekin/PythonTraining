"""x = 10

if x > 5:
    raise Exception("x 5 den buyuk deger alamaz.")"""


def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 8 karakter olmali.")
    elif not re.search("[a-z]", psw):
        raise Exception("Parola kucuk harf icermeli")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parola kucuk harf icermeli")
    elif not re.search("[0-9]", psw):
        raise Exception("Parola rakam harf icermeli")
    elif re.search("\s",psw):
        raise Exception("Parola bosluk icermemeli.")
    
password : "123456"

try:
    check_password(password)
except Exception as ex:
    print(ex)