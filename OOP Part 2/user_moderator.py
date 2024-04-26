# oop users and moderator

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
    
class Moderator(user):
    active_mods = 0
    
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.active_mods} active mods"

    def __init__(self, first, last, ages, community):
        super().__init__(first, last, ages)
        self.community = community
        Moderator.active_mods += 1

    def remove_post(self):
        return f"{self.full_name()} remove a post from {self.community}"


u1 = user("jerry","orlando", 29)
u2 = user("jerry","orlando", 29)
u3 = user("jerry","orlando", 29)
mod1 = Moderator("jessica", "o'niel", 40, "piano")
mod2 = Moderator("jessica", "o'niel", 40, "piano")
print(user.display_active_users())
print(Moderator.display_active_mods())



#print(mod.full_name())
#print(mod.community)

