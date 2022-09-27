class User:
    active_users = 0
    @classmethod
    def display_active_users(cls):
        return f"{cls.active_users} tane aktif kullanici var."
    @classmethod
    def from_string(cls,data_str):
        username,name,surname,age = data_str.split(",")
        return cls(username,name,surname,age)
    
    def __init__(self, username, name, surname, age):
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

print(User.display_active_users())

"""
print(User.display_active_users())
u1 = User("MERTTT", "Mert", "Karatekin", 20)
u2 = User("LEVENTTT", "Levent", "Ertunalilar", 37)
print(u1.userName())
print(u2.userName())
print(User.display_active_users())
print(u1.logout())
print(u2.logout())
print(User.display_active_users())
"""
u3 = User.from_string("eray_sonmez,Eray,Sonmez,24") 

print(User.display_active_users())
print(u3.username,u3.name,u3.surname,u3.age)

