class user:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active user"
    
    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self,first,last,ages):
        self.name = first
        self.last =last 
        self.age = ages
        user.active_users += 1

    def __repr__(self):
        return f"{self.name} is {self.age}"
    
    def logout(self):
        user.active_users -= 1
        return f"{self.name} has logged out"

    def full_name(self):
        return f"{self.name} {self.last}"
    
    def initials(self):
        return f"{self.name[0]}. {self.last[0]}."
    
    def fav_colors(self,thing):
        return f"{self.name} fav colors is {thing}"
    
    def is_junior(self):
        return self.age <= 60
    
    def birthday(self):
        self.age += 1
        return f"happy {self.age}th, {self.name} "

#print(user1.name, user1.age)
#print(user2.name, user2.age)
#print(user1.fav_colors("blue"))
#print(user2.initials())
#print(user1.is_junior())

#print(user.display_active_users())
#user1 = user("kevin","noufal",65)
#user2 = user("budi","setiawan",47)
#print(user.display_active_users())

bob = user.from_string("bob,mcclaren,65")
print(bob)
