class User:
    
    active_users = 0
    
    def __init__(self,username,name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1
        

    def userName(self):
        return f"{self.username} adli kullanici aktif"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.username} adli kullanici cikis yapti."
        
print(f"Aktif Kullanici : {User.active_users} ")

u1 = User("MERTTT","Mert","Karatekin",20)
u2 = User("LEVENTTT","Levent","Ertunalilar",37)

print(u1.userName())
print(u2.userName())
print(f"Aktif Kullanici : {User.active_users} ")

print(u1.logout())
print(u2.logout())

print(f"Aktif kullanici sayisi :{User.active_users}")
        